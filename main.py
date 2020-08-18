#!/usr/bin/env python
from quart import Quart, jsonify

app = Quart(__name__)
currency_service = Currency_service()

@app.route('/btc/api/v1.0/currencies', methods = ['GET'])
async def get_currencies():
    return jsonify( { 'currencies': await currency_service.get_all() } )

@app.route('/btc/api/v1.0/currencies/last', methods = ['GET'])
async def get_currency_last():
    return jsonify( { 'currency': await currency_service.get_last() } )

@app.route('/btc/api/v1.0/timer/<int:seconds>', methods = ['UPDATE'])
async def set_timer_interval(seconds: int):
    currency_service.set_timer_interval(seconds)
    return jsonify( { 'interval': currency_service.get_timer_interval() } )

@app.route('/btc/api/v1.0/timer/now', methods = ['UPDATE'])
async def update_now(seconds: int):
    return jsonify( { 'currency': await currency_service.update_now(seconds) } )

if __name__ == '__main__':
    app.run(debug = True)
