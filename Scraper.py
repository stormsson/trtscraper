import requests
import datetime

# http://docs.python-requests.org/en/v0.5.0/api/
class Scraper:
    def __init__(self,api_key=False, api_secret=False):
        self.api_key=api_key
        self.api_secret=api_secret

    def getTickerPath(self, fund="BTCEUR"):
        return "https://api.therocktrading.com/v1/funds/%s/ticker" % fund

    def sanitizeTickerData(self, data):
        dateFormat = '%Y-%m-%dT%H:%M:%S.%f%z'
        last_colon_position = data['date'].rfind(":")
        data['date'] = data['date'][:last_colon_position] + data['date'][last_colon_position+1:]
        data['date'] = datetime.datetime.strptime(data['date'], dateFormat)
        return data

    def getTicker(self, fund="BTCEUR"):
        try:
            response = requests.get(self.getTickerPath(fund))
        except Exception as e:
            raise e

        return self.sanitizeTickerData(response.json())
