from AI_Strategy_1 import TradingStrategy
from surmount.simulator import Simulator  # Assuming there's a simulator module

def main():
    # Initialize your trading strategy
    strategy_instance = TradingStrategy()
    
    # Assuming there's a Simulator class that can run a strategy
    simulator = Simulator(strategy=strategy_instance)

    # Run the strategy against historical data
    simulation_results = simulator.run()
    
    # Print or process your simulation_results here
    print(simulation_results)

if __name__ == "__main__":
    main()