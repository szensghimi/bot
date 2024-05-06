import ccxt

zalupa = ccxt.bybit().fetch_ticker("TON/USDT")

print(zalupa)