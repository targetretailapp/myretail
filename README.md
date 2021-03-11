# myRetail RESTful Service

myRetail headquartered in Richmond, VA is a rapidly growing company. We are designing a RESTful service to create an end-to-end proof of concept to make its internal data available to any number of client devices from myRetail.com to native mobile apps.

## Scenarios

1.	Retrieve product and price details for a product ID by aggregating data from multiple sources. 
2.	[Bonus] Accepts an HTTP PUT request containing a JSON request body to update the product’s price in the data store. 

## How to run the application? 

### Pre-requisites
1. Install and run [mongodb](https://docs.mongodb.com/manual/installation/).
2. Install required packages for application to run in virtual environment. 

    ```
    $ . ./utils/init-environment
    ```
     
3.  Preloading data from initial dataset, residing in data/data.json
    
    - If needed, update DB host and port details in config.ini. Default hostname and port in config are localhost and 27017 respectively.  
```
$ python initialDataLoad.py
```

### Launch Application
Execute main.py. Application runs on port 5000. 

```
$ python main.py
```

## Sample output

```
$ curl http://localhost:5000/products/13860428
{
    "product_name": "The Big Lebowski (Blu-ray)",
    "product_price": {
        "_id": 13860428,
        "current_price": {
            "currency_code": "USD",
            "value": 99.99
        },
        "product_id": 13860428
    }
}                                        
``` 

## Further Investment

1. Database authentication
2. Introduce Logging 
3. Better error handling  
4. Write test cases
5. Dockerize the application 
