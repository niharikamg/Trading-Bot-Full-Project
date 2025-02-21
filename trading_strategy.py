import pandas as pd
import yfinance as yf
import talib

df = yf.download("AAPL", period="60d", interval="1h")

df["EMA_10"] = talib.EMA(df["Close"], timeperiod=10)
df["EMA_50"] = talib.EMA(df["Close"], timeperiod=50)

def trading_strategy(data):
    buy_signals = []
    sell_signals = []

    for i in range(len(data)):
        if data["EMA_10"][i] > data["EMA_50"][i]:
            buy_signals.append(data["Close"][i])
            sell_signals.append(None)
        elif data["EMA_10"][i] < data["EMA_50"][i]:
            sell_signals.append(data["Close"][i])
            buy_signals.append(None)
        else:
            buy_signals.append(None)
            sell_signals.append(None)

    return buy_signals, sell_signals

df["Buy"], df["Sell"] = trading_strategy(df)
print(df.tail())
