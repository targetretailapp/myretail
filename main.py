from myretail.app import app

# Below two should go away
# from myretail.redsky import Redsky
from myretail.pricedetails import PriceDetails

if __name__ == "__main__":
    app.run(port=5000)

    # Below is temp work to see if DB part of the code is working
    # print(db.get_price_by_product_id(13860428))
    # p=PriceDetails()
    p.pricedetails(13860428)





