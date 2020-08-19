# About
This service provide save info about rate Bitcoin from coinmarketcap.com.
# How to run
## Get token
Go to https://pro.coinmarketcap.com/account/ and get your token.
## Run via docker
```bash
sudo RATE_BTC_AUTH=YOUR-TOKEN-HERE docker-compose up
```
If you see ```btc_runner_1    |  * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)``` and ```gateway_1       | /docker-entrypoint.sh: Configuration complete; ready for start up```, you can connect to server http://localhost/
You can also append RATE_BTC_INTERVAL_UPDATE:
```bash
sudo RATE_BTC_AUTH=YOUR-TOKEN-HERE RATE_BTC_INTERVAL_UPDATE=600 docker-compose up
```
## Run via python
Run:
```bash
RATE_BTC_AUTH=YOUR-TOKEN-HERE ./main.py
```
Or:
```bash
echo YOUR-TOKEN-HERE | ./main.py
```
Get help:
```bash
./main.py --help
```
# Environments
| name                     | help                                                |
|--------------------------|-----------------------------------------------------|
| RATE_BTC_DB              | str info about DB. Default: sqlite:////tmp/btc.db   |
| RATE_BTC_AUTH            | Authkey from another API                            |
| RATE_BTC_INTERVAL_UPDATE | Interval to autosave from API to DB. Default: 300.0 |
| RATE_BTC_PORT            | Port (listener) of flask server. Default 5000.      |

# API
| method | urn                                  | help                                                                           |
|--------|--------------------------------------|--------------------------------------------------------------------------------|
| GET    | /                                    | Get available urns                                                             |
| GET    | /btc/api/v1.0/                       | Get available urns                                                             |
| GET    | /btc/api/v1.0/currencies/            | Get all rates bitcoin                                                          |
| GET    | /btc/api/v1.0/currencies/last/       | Get last rate bitcoin                                                          |
| PUT    | /btc/api/v1.0/timer/<float:seconds>/ | Change timer interval                                                          |
| PATCH  | /btc/api/v1.0/timer/now/             | Get Bitcoin rate and put result in DB, return actual rate without id and stamp |

