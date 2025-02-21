import pandas as pd
import yfinance as yf
import talib

df = yf.download("AAPL", period="60d", interval="1h")

df["EMA_10"] = talib.EMA(df["Close"], timeperiod=10)
df["EMA_50"] = talib.EMA(df["Close"], timeperiod=50)
df["RSI"] = talib.RSI(df["Close"], timeperiod=14)
df["MACD"], df["MACD_signal"], _ = talib.MACD(df["Close"], fastperiod=12, slowperiod=26, signalperiod=9)

print(df.tail())
