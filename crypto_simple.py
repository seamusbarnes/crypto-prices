import requests

def get_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()

    return data['price']

def display_prices(symbols, unit):
    align = {'left': 8, 'right': 15}
    
    print('\nPrices - Current')
    header = f"{'Symbol'.ljust(align['left'])} {'Price (USDT)'.rjust(align['right'])}"
    print(header)
    print('-' * len(header))

    for symbol in symbols:
        price = get_binance_price(f'{symbol}{unit}')
        print(f"{symbol.ljust(align['left'])} {f'${float(price):.2f}'.rjust(align['right'])}")

    return

if __name__ == "__main__":
    
    unit = 'USDT' 
    symbols = ['BTC', 'ETH', 'LINK', 'DOT', 'ADA']

    display_prices(symbols, unit)