#!/usr/bin/env python
import aiohttp
import asyncio

async def get_btc(authkey: str):
    """
    Gets the current bitcoin rate from server.
    :param authkey: Authkey from pro-api.coinmarketcap.com.
    """
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', headers = {'X-CMC_PRO_API_KEY': authkey, 'Accept': 'application/json'}, params = {'id': 1})
            j = (await response.json())['data']['1']
            currency = list(j['quote'].keys())[0]
            return {'currency': currency, 'price': j['quote'][currency]['price']}
    except:
        return None

async def main():
    print(await get_btc(input("authkey: ")))

if __name__ == "__main__":
    asyncio.run(main())
