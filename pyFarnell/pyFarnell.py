import requests

class Farnell():

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.base_url = 'https://api.element14.com/catalog/products'

    def get_part_number(self, partNum):
        """Gets part information where **partNum** is Farnell's product ID"""
        params = {
                   'callInfo.responseDataFormat': 'JSON',
                   'term': 'id:' + str(partNum),
                   'storeInfo.id': 'sk.farnell.com',
                   'callInfo.apiKey': self.apiKey,
                 }
        r = requests.get(self.base_url, params = params)
        if r.status_code != 200:
            raise Exception("Developer apiKey not active - contact Farnell representative.")
        return r.__dict__
