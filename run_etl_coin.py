"""Script for collect data of API: https://coinmarketcap.com/api.

    Endpoints that return data around cryptocurrencies such as ordered cryptocurrency lists or price and volume data.
    Latest market ticker quotes and averages for cryptocurrencies and exchanges.



"""

from etl.etl_coinmarket import ETLCoinmarket
from utils.engines import get_engine, get_api

if __name__ == "__main__":
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': get_api('api_key_coinmarketcap'),
    }
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'BRL'
    }

    input = {
        'url': url,
        'params': parameters,
        'headers': headers}

    output = {
        'name': 'tb_coins',  # table_name
        'con': get_engine('COIN')
    }

    market = ETLCoinmarket(input=input, output=output)
    market.controller_etl()
