import yaml

class Config:
    def __init__(self):

    def readDB(self, path):
        with open(path) as f:
            dbConfig = yaml.safe_load(f)
        return dbConfig