import ccxt

symbol = 'uBTCUSD'
exchange = ccxt.binance({    # change to any exchange you want
    'enableRateLimit':True,
    'apiKey': 'your api key',    # need to have at least one account in that exchange
    'secret': 'your key',
})

def ob():
    ob = exchange.fetch_order_book(symbol)
    return ob

print(ob()).   # return the object, only one timestamp per run with n-dim array of format [bid price, bid volume], [ask price, ask volume]
