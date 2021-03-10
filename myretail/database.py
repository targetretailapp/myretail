# REFERENCE: https://realpython.com/introduction-to-mongodb-and-python/#managing-nosql-databases-with-mongodb

import os
import configparser
from pymongo import MongoClient, errors
import json

class Database():
    """
    Database class performs all Mongodb related functions, including:
    1. Preloading data from initial dataset, residing in data/data.json
    2. Fetches price details for a given product_id
    3. Updates price for a given product_id
    """
    def __init__(self):
        # Loading & reading from config.ini config file
        config = configparser.ConfigParser()
        try:
            config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../config.ini")
        except IOError:
            raise ValueError("Could not find or open file {0}".format(config_path))
        except:
            raise ValueError("{}".format(config_path))

        config.read(config_path)

        # Below code snippet connects to mongodb while fetching config details from config.ini
        self.dbhost = config.get('database', 'host')
        self.dbport = config.get('database', 'port')
        self.dbname = config.get('database', 'database')

        dbclient = MongoClient(host=self.dbhost, port=int(self.dbport))

        self.db = dbclient[self.dbname]

    def dataload(self):
        """
        Loads data in collection, price, of product_proce database
        :return:
        """
        collection_product_price=self.db['price']
        with open('data/data.json') as d:
            price_data = json.load(d)

        # Reference: https://stackoverflow.com/questions/44838280/how-to-ignore-duplicate-key-errors-safely-using-insert-many
        try:
            inserted=collection_product_price.insert_many(price_data, ordered = False)
            print("{} records inserted", len(inserted))
        except errors.BulkWriteError as e:
            print(e.details['writeErrors'])

    def get_price_by_product_id(self, product_id):
        """
        Fetches price details for a given product_id
        :param product_id:
        :return:
        """
        return self.db.price.find_one({"product_id": product_id})

    def update_price_by_product_id(self, updated_product):
        """
        IMPLEMENTATION PENDING
        Updates product price for a given product_id
        :param updated_product:
        :return:
        """
        pass










