import pymongo
from pymongo.results import UpdateResult

from libs.user import User

class DBConnection:

    def __init__(self, uri):
        self.uri = uri
        self.client = None
        self.db = None
        self.collection = None
    
    def get_client(self):
        self.client = pymongo.MongoClient(self.uri) 
        return self.client
    
    def get_users_collection(self):
        self.db = self.client['goodmorning']
        self.collection = self.db['users']
        return self.collection
    
    def add_user(self, user_dict):
        return self.collection.update({'name': user_dict['name']}, {'$set': {'sites' : user_dict['sites']}, '$set': {'background_img' : user_dict['background_img']}}, upsert=True)
    
    def update_user(self, user_dict):
        pointer = self.collection.find({'name': user_dict['name']}, {"sites":1, "background_img":1})
        for e in pointer:
            if e['sites'] == user_dict['sites']:
                if e['background_img'] == user_dict['background_img']:
                    return 0
                self.collection.update()
            print(e['sites'])
            print(e['background_img'])

    

