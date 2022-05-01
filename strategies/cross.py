import math
import backtrader as bt
from pandas import Period

class CrossSMA(bt.Strategy):
    params = (('fast', 20),('slow', 30), ('order_percentage', 0.10), ('ticker', 'SPY'), ('stop_loss', .95 ), ('trail', False), ('buy_limit', False))

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.fast, plotname='20 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.params.slow, plotname='30 day moving average'
        )

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

        self.dataclose = self.datas[0].close
        self.order = None

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))

                self.buy(size=self.size)
                

        if self.position.size > 0:
            stop_price = self.data.close[0] * (1.0 - self.params.stop_loss)
            print(self.buy)
            print(stop_price)
            self.close(price=stop_price)

        if self.crossover < 0:
        #Here is where add more to sell params (if:)
            print("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
            self.close()
                    

