#!/usr/bin/env python3

import requests

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()

    return data['price']

def get_daily_open_price(symbol, interval='1d'):
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': 2
    }
    response = requests.get(url, params=params)
    data = response.json()

    yesterday_price = float(data[0][1])
    today_price = float(data[1][1])
    percent_move = (today_price-yesterday_price)/yesterday_price

    return today_price, percent_move

def get_kline_data(symbol, interval='1d', limit=2):
    '''
    returns list of list, each list representing data from a particular candle (the length of which is given by the interval) in order

    the lists give the following data:
    index, data name
    0, kline open time
    1, open price
    2, low price
    3, close price
    4, volume
    5, kline close time
    6, quote asset volume
    7, number of trades
    8, taker buy base asset volume
    9, taker buy quote asset volume
    10, unused field, ignore

    the most important indices are obviously 1 (open price) and 0 (open time)

    '''
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Example usage of the functions
if __name__ == "__main__":
    
    unit = 'USDT' 
    symbols = ['BTC', 'ETH', 'LINK', 'DOT', 'ADA']

    print('\nPrices - Current')
    header = f"{'Symbol'.ljust(8)} {'Price (USDT)'.rjust(15)}"
    print(header)
    print('-' * len(header))

    for symbol in symbols:
        price = get_binance_price(f'{symbol}{unit}')
        print(f"{symbol.ljust(8)} {f'${float(price):.2f}'.rjust(15)}")

    print('\nPrices - Daily Open')
    header = f"{'Symbol'.ljust(8)} {'Open Price (USDT)'.rjust(15)} {'Change (%)'.rjust(12)}"
    print(header)
    print('-' * len(header))

    for symbol in symbols:
        price, percent = get_daily_open_price(f'{symbol}{unit}')
        print(f"{symbol.ljust(8)} {f'${float(price):.2f}'.rjust(15)} {f'{percent:.4f}'.rjust(12)}")

    data = get_kline_data('BTCUSDT', interval='1d', limit=10)
    data = [data[i][1] for i in range(len(data))]
