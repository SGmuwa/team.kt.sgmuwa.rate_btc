#!/usr/bin/env python

from flask import Flask, jsonify
from currency_service import Currency_service

app = Flask(__name__)
currency_service = Currency_service()


@app.route('/btc/api/v1.0/currencies', methods=['GET'])
def get_currencies():
    return jsonify({'currencies': currency_service.get_all()})


@app.route('/btc/api/v1.0/currencies/last', methods=['GET'])
def get_currency_last():
    return jsonify({'currency': currency_service.get_last()})


@app.route('/btc/api/v1.0/timer/<int:seconds>', methods=['UPDATE'])
def set_timer_interval(seconds: int):
    currency_service.interval = seconds
    return jsonify({'interval': currency_service.interval})


@app.route('/btc/api/v1.0/timer/now', methods=['UPDATE'])
def update_now():
    return jsonify({'currency': currency_service.update_now()})


if __name__ == '__main__':
    app.run(debug=False)
