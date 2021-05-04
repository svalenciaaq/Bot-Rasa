import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def inititialize():
        client = pymongo.MongoClient(Database.URI)
        print(client)
        Database.DATABASE = client['rasa']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)    