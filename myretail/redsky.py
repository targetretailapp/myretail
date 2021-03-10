from urllib.parse import urljoin
import requests
import os
import configparser
from myretail.database import Database
from myretail.errors import ProductNotFoundError

class Redsky():
    """
    Redsky class retrieves product name from redsky.target.com
    """
    def __init__(self):
        config = configparser.ConfigParser()
        try:
            config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../config.ini")
        except IOError:
            raise ValueError("Could not find or open file {0}".format(config_path))
        except:
            raise ValueError("{}".format(config_path))

        config.read(config_path)
        self.endpoint = config.get('redsky', 'product_endpoint')
        self.excludes = config.get('redsky', 'product_endpoint_exclude_fields')
        self.key = config.get('redsky', 'key')

    def fetch_name(self, product_id):
        """
        Retrieves product name for a given product_id from redsky.target.com
        :param product_id:
        :return:
        """
        product_url = urljoin(self.endpoint, str(product_id)) + "?excludes={}".format(self.excludes) + "&key={}".format(self.key)

        result = requests.get(product_url)

        if result.status_code != requests.codes["ok"]:
            raise ProductNotFoundError("could not find product name for ID {}".format(product_id))

        data = result.json()

        try:
            name = data["product"]["item"]["product_description"]["title"]
        except KeyError:
           name = None

        return name



