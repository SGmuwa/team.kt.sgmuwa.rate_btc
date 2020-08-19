#!/usr/bin/env python
import requests
import sys

def get_btc(authkey: str):
    """
    Gets the current bitcoin rate from server.
    :param authkey: Authkey from pro-api.coinmarketcap.com.
    """
    j = None
    try:
        j = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            headers = {'X-CMC_PRO_API_KEY': authkey, 'Accept': 'application/json'},
            params = {'id': 1})
        j = j.json()['data']['1']
        currency = list(j['quote'].keys())[0]
        return {'currency': currency, 'price': j['quote'][currency]['price']}
    except Exception as e:
        print(e, type(e), j, file=sys.stderr)
        try:
            print(j.text, j.headers, file=sys.stderr)
        except:
            pass
        return None

if __name__ == "__main__":
    print(get_btc(input("authkey: ")))
