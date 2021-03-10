import os.path
from flask import jsonify, Response, make_response
import configparser
import json
from myretail.database import Database
from myretail.redsky import Redsky

class PriceDetails():
    """
    PriceDetails class calls redsky.target.com to fetch product name, and mongodb to fetch price details for a give product_id.
    It then constructs a json response from this data and returns to the caller.
    """
    def __init__(self):
        self.db = Database()
        self.redsky=Redsky()

    def pricedetails(self, product_id):
        """
        Fetches product_name from redsky.target.com, and product_price from mongo DB.
        :param product_id:
        :return:
        """
        product={}
        product['product_price'] = self.db.get_price_by_product_id(int(product_id))
        product['product_name'] = self.redsky.fetch_name(product_id)

        return(json.dumps(product, indent=4, sort_keys=True))

