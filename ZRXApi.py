import requests


# http://docs.python-requests.org/en/v0.5.0/api/
class ZRXApi:
    MAX_ORDERBOOK_LENGTH = 20
    baseDomain = "https://api.radarrelay.com/0x/v0"
    # def __init__(self, domain):
    #     self.baseDomain = domain


    def __init__(self):
        self.lastResponse = False

    def getLastResponseHeaders(self):
        try:
            headers = self.lastResponse.headers
        except Exception as e:
            headers = {}

        return headers


    def getOrderBookPath(self, baseTokenAddress, quoteTokenAddress):
        return self.baseDomain + "/orderbook?baseTokenAddress=%s&quoteTokenAddress=%s" % (baseTokenAddress, quoteTokenAddress)

    def getTokenPairsPath(self, tokenA, tokenB):
        return self.baseDomain + "/token_pairs?tokenA=%s&tokenB=%s" % (tokenA, tokenB)



    def getTokenPairs(self, tokenA, tokenB):
        try:
            response = requests.get(self.getTokenPairsPath(tokenA, tokenB))
        except Exception as e:
            raise e

        self.lastResponse = response
        return response.json()

    def getOrderBook(self, baseTokenAddress, quoteTokenAddress):
        try:
            response = requests.get(self.getOrderBookPath(baseTokenAddress, quoteTokenAddress))
        except Exception as e:
            raise e

        return response.json()