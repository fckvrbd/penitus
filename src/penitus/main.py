"""A script to use the coinpaprika API"""

import json

import requests


class Penitus:

    """A class to use the coinpaprika API"""

    def __init__(self):
        self.base_url = "https://api.coinpaprika.com/v1"

    def _init_functions(self, data, *keys):
        try:
            return self._dumps(self._get_key(data, keys))
        except KeyError as err:
            raise err

    def _request(self, args: str):
        req = requests.get("{}{}".format(self.base_url, args))
        if req.status_code != 200:
            return "Wait please!"
        return req.json()

    @staticmethod
    def _dumps(_json):
        return json.dumps(_json, indent=4)

    @staticmethod
    def _get_key(data, *keys):
        for _list in keys:
            for _other_list in _list:
                for k in _other_list:
                    data = data[k]
                return data

    def global_market(self, *keys):
        """Gets market overview"""
        data = self._request("/global")
        return self._init_functions(data, keys)

    def coins(self, *keys):
        """Get all coins"""
        data = self._request("/coins")
        return self._init_functions(data, keys)

    def get_coin(self, coin, *keys):
        """Get certain coin"""
        data = self._request("/coins/{}".format(coin))
        return self._init_functions(data, keys)

    def get_coin_twitter(self, coin, *keys):
        """Get certain coin tweets"""
        data = self._request("/coins/{}/twitter".format(coin))
        return self._init_functions(data, keys)
