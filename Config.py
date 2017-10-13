import yaml

class Config:

    @staticmethod
    def readDB(path):
        with open(path) as f:
            dbConfig = yaml.safe_load(f)
        return dbConfig