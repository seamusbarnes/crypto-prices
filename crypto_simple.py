#!/usr/bin/env python3

import requests

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()

    return data['price']

# Example usage of the functions
if __name__ == "__main__":
    
    unit = 'USDT' 
    symbols = ['BTC', 'ETH', 'LINK', 'DOT', 'ADA']

    align_left = 8
    align_right = 15
    print('\nPrices - Current')
    header = f"{'Symbol'.ljust(align_left)} {'Price (USDT)'.rjust(align_right)}"
    print(header)
    print('-' * len(header))

    for symbol in symbols:
        price = get_binance_price(f'{symbol}{unit}')
        print(f"{symbol.ljust(align_left)} {f'${float(price):.2f}'.rjust(align_right)}")
