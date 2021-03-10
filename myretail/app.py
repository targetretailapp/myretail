from flask import Flask, Response
from flask_restful import Resource, Api
# from requests import api
# import json
from myretail.pricedetails import PriceDetails

app = Flask(__name__)
api = Api(app)

class Products(Resource):
    def get(self, product_id):
        # get price and name details for given product id.
        details = PriceDetails()
        data = details.pricedetails(product_id)
        response = Response(content_type="application/json")
        response.set_data(data)
        response.status_code = 200
        return response

        # print(type(details.pricedetails(product_id)))
        # if data == None:
        #     return (None, 404)
        # else:
        #     response = Response(content_type="application/json")
        #     response.set_data(data)
        #     response.status_code = 200
        #     return response


api.add_resource(Products, '/products/<int:product_id>') # http://<hostname>:<port>/products/{product_id}

