#Type code here# Main function to run the backtest
if __name__ == "__main__":
    from surmount.main import run_backtest
    from datetime import datetime, timedelta
    
    # Define backtest period (5 years)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5*365)
    
    # Run the backtest
    result = run_backtest(
        BollingerBandsStrategy(),
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d")
    )
    
    # Print results
    print("Backtest Results:")
    print(result)