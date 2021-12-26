import os
import pymongo


class Database:
    def __init__(self):
        self.client = pymongo.MongoClient(os.environ.get("LOCAL_CONNECTION"))

        self.db = self.client.get_database(os.environ.get("DB_NAME"))

    def insert_object(self, object_dictionary, collection):
        collection = self.db.get_collection(collection)
        collection.insert(object_dictionary)

    def insert_many_objects(self, object_dictionary, collection):
        collection = self.db.get_collection(collection)
        collection.insert_many(object_dictionary)

    def select_object(self, collection, where):
        collection = self.db.get_collection(collection)
        results = list(collection.find(where))

        return results

    def select_one_object(self, collection, where):
        collection = self.db.get_collection(collection)
        results = collection.find_one(where)

        return results

    def update_object(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$set': object_dictionary}, upsert=True)

    def update_objects(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$set': object_dictionary}, upsert=False, multi=True)

    def update_rename(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$rename': object_dictionary})

    def update_array(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$addToSet': object_dictionary})

    def update_array_push(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$push': object_dictionary}, upsert=True)

    def delete_array(self, object_dictionary, collection, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$pullAll': object_dictionary}, upsert=True)

    def delete_many(self, collection, where):
        collection = self.db.get_collection(collection)

        return collection.delete_many(where)

    def delete_one(self, collection, where):
        collection = self.db.get_collection(collection)

        return collection.delete_one(where)

    def count_documents(self, collection, where):
        collection = self.db.get_collection(collection)

        return collection.count_documents(where)

    def get_object(self, collection=''):
        if collection != '':
            collection = self.db.get_collection(collection)

            return collection

        return self.db

    def increment_field(self, collection, field, where):
        collection = self.db.get_collection(collection)

        return collection.update(where, {'$inc': {field: 1}})

    def select_all_objects(self, collection):
        collection = self.db.get_collection(collection)

        return list(collection.find({}))
