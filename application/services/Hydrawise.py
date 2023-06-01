import os

import requests


class Hydrawise:
    def __init__(self):
        self.API_LOCATION = 'https://api.hydrawise.com/api/v1'
        self.API_KEY = os.environ.get('HYDRAWISE_API_KEY')
        self.zone_map = self._build_zone_map()

    def _request(self, path: str, params: dict) -> dict:
        res = {}
        try:
            res = requests.get(self.API_LOCATION + path, params=params).json()
        except Exception as e:
            raise e
        return res

    def _build_zone_map(self):
        relay_map = {}
        schedules = self.get_schedules()
        for relay in schedules['relays']:
            relay_map[str(relay['relay'])] = relay['relay_id']
        return relay_map

    def get_schedules(self, controller_id=None) -> dict:
        path = '/statusschedule.php'
        params = dict(api_key=self.API_KEY)
        if controller_id:
            params['controller_id'] = controller_id
        return self._request(path, params)

    def get_customer_details(self) -> dict:
        path = '/customerdetails.php'
        params = dict(api_key=self.API_KEY)
        return self._request(path, params)

    def run_zone(self, zone_id: str, run_time: int) -> dict:
        path = '/setzone.php'
        params = dict(api_key=self.API_KEY, action='run', custom=run_time, relay_id=self.zone_map[zone_id])
        return self._request(path, params)
