import backtrader as bt
import yfinance as yf

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.ema10 = bt.indicators.ExponentialMovingAverage(period=10)
        self.ema50 = bt.indicators.ExponentialMovingAverage(period=50)

    def next(self):
        if self.ema10 > self.ema50:
            self.buy()
        elif self.ema10 < self.ema50:
            self.sell()

cerebro = bt.Cerebro()
df = yf.download("AAPL", period="60d", interval="1h")
data = bt.feeds.PandasData(dataname=df)
cerebro.adddata(data)
cerebro.addstrategy(MyStrategy)
cerebro.run()
cerebro.plot()
