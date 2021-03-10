from myretail.database import Database

def dataLoad():
    """
    Performs initial data load in product_price database from initial data dump (in data/data.json)
    :return:
    """
    db=Database()
    db.dataload()

dataLoad()

