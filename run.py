import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.cross import CrossSMA
import datetime

cerebro =bt.Cerebro()

cerebro.broker.set_cash(200000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='qqq.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2020, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 12, 31),
    reverse=False)

cerebro.adddata(data)
cerebro.addstrategy(CrossSMA)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()