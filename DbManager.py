import pymongo

class DbManager:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
