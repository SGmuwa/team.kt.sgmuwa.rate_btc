#!/usr/bin/env python
import requests

def get_btc(authkey: str):
    """
    Gets the current bitcoin rate from server.
    :param authkey: Authkey from pro-api.coinmarketcap.com.
    """
    try:
        j = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            headers = {'X-CMC_PRO_API_KEY': authkey, 'Accept': 'application/json'},
            params = {'id': 1}).json()['data']['1']
        currency = list(j['quote'].keys())[0]
        return {'currency': currency, 'price': j['quote'][currency]['price']}
    except:
        return None

if __name__ == "__main__":
    print(get_btc(input("authkey: ")))
