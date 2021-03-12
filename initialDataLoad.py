from myretail.database import Database

def dataLoad():
    """
    Performs initial data load in product_price database from initial data dump (in data/data.json)
    :return:
    """
    db=Database()
    db.dataload()
    
if __name__ == "__main__":
    dataLoad()

