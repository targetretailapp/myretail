class ProductNotFoundError(Exception):
    def __init__(self, message):
        super(ProductNotFoundError, self).__init__(message, "Product not found", 404)

## Add additional error handling here.