import ccxt

symbol = 'uBTCUSD'
exchange = ccxt.binance({    # change to any exchange you want
    'enableRateLimit':True,
    'apiKey': 'your api key',
    'secret': 'your key',
})

def ob():
    ob = exchange.fetch_order_book(symbol)
    return ob

print(ob())