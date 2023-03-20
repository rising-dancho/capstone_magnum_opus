import time
import os
import urllib.parse
import hashlib
import hmac
import base64

import requests

class Kraken(object):
    api_url = "https://api.kraken.com"

    # Get from: https://www.okcoin.com/account/my-api/create (Must be signed in obviously)
    api_key = "/sk12162sZfc6L7kohoUg7dpPOQfV88ejSwNUpLHvi2UhaX4HwmzT0BX"    
    api_sec = "ejLSo7/JmSeBeBW5y33vxJC7QoK/o7yJyYyl9eHyXONJn45Wt/Q639xboW399BJiWf2eiefFuEqQ0qOZ8Pi/mQ=="

    def get_kraken_signature(self, urlpath, data):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self.api_sec), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    # Attaches auth headers and returns results of a POST request
    def kraken_request(self, uri_path, data):
        headers = {}
        headers['API-Key'] = self.api_key
        # get_kraken_signature() as defined in the 'Authentication' section
        headers['API-Sign'] = self.get_kraken_signature(uri_path, data)             
        req = requests.post((self.api_url + uri_path), headers=headers, data=data)
        print(req.status_code)
        return req

    def place_order(self, volume, pair, buy_price, order_type="buy"):
        # Construct the request and print the result
        resp = self.kraken_request('/0/private/AddOrder', {
            "nonce": str(int(1000*time.time())),
            "ordertype": "limit",
            "type": order_type,
            "volume": volume,
            "pair": pair,
            "price": buy_price
        })

        return resp.json()

    def get_balance(self):
        resp = self.kraken_request('/0/private/Balance', {
            "nonce": str(int(1000*time.time()))
        })

        return resp.json()

    def cancel_order(self, order_id):
        resp = self.kraken_request('/0/private/CancelOrder', {
            "nonce": str(int(1000*time.time())),
            "txid": order_id
        })

        return resp.json()


if __name__ == '__main__':
    # Construct the request and print the result
    kr = Kraken()
    resp = kr.get_balance()
    print(resp)