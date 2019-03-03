from pymongo import MongoClient


class MongoDB():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['collaboration_net_db']
        self.user_collection = self.db['users']
