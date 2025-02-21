import time
import ccxt
import yfinance as yf
import talib

binance = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret'
})

def place_order(symbol, side, amount):
    order = binance.create_order(symbol, 'market', side, amount)
    print(f"Order Placed: {order}")

while True:
    ticker = binance.fetch_ticker("BTC/USDT")
    print(f"BTC Price: ${ticker['last']}")

    df = yf.download("AAPL", period="60d", interval="1h")
    df["EMA_10"] = talib.EMA(df["Close"], timeperiod=10)
    df["EMA_50"] = talib.EMA(df["Close"], timeperiod=50)

    if df["EMA_10"].iloc[-1] > df["EMA_50"].iloc[-1]:
        place_order('BTC/USDT', 'buy', 0.001)
    elif df["EMA_10"].iloc[-1] < df["EMA_50"].iloc[-1]:
        place_order('BTC/USDT', 'sell', 0.001)

    time.sleep(60)
