import ccxt

binance = ccxt.binance()
symbol = 'BTC/USDT'

ticker = binance.fetch_ticker(symbol)
print(f"Current {symbol} Price: ${ticker['last']}")
