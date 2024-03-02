import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import datetime

retry_strategy = Retry(
    total=None,
    status_forcelist=tuple(range(401, 600)),
    method_whitelist=["GET"],
    backoff_factor=1
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)

def fetch_ncn():
    r = http.get("https://explorer.nucoin.com.br/files/blockchain/price_history.json")
    data = r.json()
    data = [val for val in data['prices'].values()].pop()
    return float(data['brlBalance']) / float(data['ncnBalance'])

def fetch_btc():
    r = http.get("http://economia.awesomeapi.com.br/json/last/BTC-BRL")
    price_btc = r.json()
    btc_hi = float(price_btc['BTCBRL']['high'])
    btc_lo = float(price_btc['BTCBRL']['low'])
    BTC_BRL = (btc_hi + btc_lo) / 2
    return BTC_BRL

def fetch_eth():
    r = http.get("http://economia.awesomeapi.com.br/json/last/ETH-BRL")
    price_btc = r.json()
    ETH_hi = float(price_btc['ETHBRL']['high'])
    ETH_lo = float(price_btc['ETHBRL']['low'])
    ETH_BRL = (ETH_hi + ETH_lo) / 2
    return ETH_BRL

