from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import BB
from surmount.logging import log

class BollingerBandsStrategy(Strategy):
    def __init__(self):
        # Specifies the asset(s) the strategy targets
        self.tickers = ["SPY"]

    @property
    def assets(self):
        return self.tickers

    @property
    def interval(self):
        # "1day" interval for daily trading; adjust accordingly if needed
        return "1day"

    @property
    def data(self):
        # No additional data sources needed for this strategy
        return []

    def run(self, data):
        # Extract the ohlcv (Open, High, Low, Close, Volume) data for SPY
        ohlcv_data = data["ohlcv"]
        recent_data = ohlcv_data[-1]  # Get the most recent data point

        # Calculate Bollinger Bands for SPY with default parameters
        # Note: You might need to adjust length and std params based on your strategy specifics
        bb_result = BB("SPY", ohlcv_data, length=20, std=2)
        upper_band = bb_result['upper'][-1]
        close_price = recent_data["SPY"]["close"]

        # Determine action based on Bollinger Bands and recent closing price
        allocation = {}
        if close_price > upper_band:
            # Price is above the upper Bollinger Band, consider entering or holding the position
            allocation["SPY"] = 1.0  # Allocate 100% of the portfolio to SPY
        else:
            # Price is below the upper Bollinger Band, consider exiting the position
            allocation["SPY"] = 0.0  # Allocate 0% of the portfolio to SPY, i.e., exit the position
        
        return TargetAllocation(allocation)

# Note: You would then initiate a backtest using this strategy over 5 years of SPY data within your backtesting environment.