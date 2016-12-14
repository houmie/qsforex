from __future__ import print_function

from configs import config_base as config
from backtest.backtest import Backtest
from data.price import HistoricCSVPriceHandler
from execution.execution import SimulatedExecution
from portfolio.portfolio import Portfolio
from strategy.strategy import MovingAverageCrossStrategy

if __name__ == "__main__":
    # Trade on GBP/USD and EUR/USD
    pairs = ["GBPUSD", "EURUSD"]

    # Create the strategy parameters for the
    # MovingAverageCrossStrategy
    strategy_params = {
        "short_window": 500,
        "long_window": 2000
    }

    # Create and execute the backtest
    backtest = Backtest(
        pairs, HistoricCSVPriceHandler,
        MovingAverageCrossStrategy, strategy_params,
        Portfolio, SimulatedExecution,
        equity=config.EQUITY
    )
    backtest.simulate_trading()
