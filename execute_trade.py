import ccxt

binance = ccxt.binance({
    'apiKey': 'your_api_key',
    'secret': 'your_api_secret'
})

def place_order(symbol, side, amount):
    order = binance.create_order(symbol, 'market', side, amount)
    print(f"Order Placed: {order}")

place_order('BTC/USDT', 'buy', 0.001)
