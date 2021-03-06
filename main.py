#!/usr/bin/env python

import sys
if __name__ == '__main__' and ('-h' in sys.argv or '--help' in sys.argv):
    print('''
This service get currency BTC from other API and save it in DB.

envs:
RATE_BTC_DB	str info about DB. Default: sqlite:////tmp/btc.db
RATE_BTC_AUTH	Authkey from another API
RATE_BTC_INTERVAL_UPDATE	Interval to autosave from API to DB. Default: 300.0
RATE_BTC_PORT	Port (listener) of flask server. Default 5000.

args:
-h	get this help
'''); quit()

from flask import Flask, jsonify
from currency_service import Currency_service
import os
from custom_json_encoder import set_custom_json_encoder


db_info: str = os.getenv('RATE_BTC_DB', 'sqlite:////tmp/btc.db')
authkey: str = os.environ.get('RATE_BTC_AUTH')
if authkey is None:
    authkey = input('authkey: ')
try:
    interval: float = float(os.environ['RATE_BTC_INTERVAL_UPDATE'])
except:
    interval: float = 60.*5
try:
    port: int = int(os.environ['RATE_BTC_PORT'])
except:
    port: int = 5000


if __name__ == '__main__':
    app = Flask(__name__)
    currency_service = Currency_service(db_info, authkey, interval)

set_custom_json_encoder(app)


@app.route('/btc/api/v1.0/currencies/', methods=['GET'])
def get_currencies():
    return jsonify({'currencies': currency_service.get_all()})


@app.route('/btc/api/v1.0/currencies/last/', methods=['GET'])
def get_currency_last():
    return jsonify({'currency': currency_service.get_last()})


@app.route('/btc/api/v1.0/timer/<float:seconds>/', methods=['PUT'])
def set_timer_interval(seconds: float):
    currency_service.interval = seconds
    return jsonify({'interval': currency_service.interval})


@app.route('/btc/api/v1.0/timer/now/', methods=['PATCH'])
def update_now():
    return jsonify({'currency': currency_service.update_now()})

@app.route('/', methods=['GET'])
@app.route('/btc/api/v1.0/', methods=['GET'])
def get_api():
    return jsonify({'api': [
        {'url': '/btc/api/v1.0/currencies/', 'method': 'GET'},
        {'url': '/btc/api/v1.0/currencies/last/', 'method': 'GET'},
        {'url': '/btc/api/v1.0/timer/<float:seconds>/', 'method': 'PUT'},
        {'url': '/btc/api/v1.0/timer/now/', 'method': 'PATCH'},
        {'url': '/btc/api/v1.0/', 'method': 'GET'}]})


if __name__ == '__main__':
    app.run(debug=False, port=port, host='0.0.0.0')
