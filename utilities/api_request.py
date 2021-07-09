import json

import requests

class APIRequest:
    def __init__(self, token, endpoint):
        self.token = token
        self.base_endpoint = endpoint
        self.headers = {'X-TrackerToken': token, 'Content-Type': 'application/json'}

    def execute_request(self, method, endpoint, data=None):
        api_url = "{}{}".format(self.base_endpoint, endpoint)
        if data:
            response = requests.request(method, api_url, headers=self.headers, data=json.dumps(data))
        else:
            response = requests.request(method, api_url, headers=self.headers)
        return response
