import ccxt

def price(coin: str):
    coin = coin.upper().strip()

    ticker_info = ccxt.bybit().fetch_ticker(f'{coin}/USDT')

    buy_price = round(float(ticker_info['ask']), 2)
    percentage = ticker_info['percentage']

    return (f"<b>{ticker_info['symbol']}</b>\n\n"
            f"1 {coin} ≈ {buy_price} USDT | {percentage} %"
            )



