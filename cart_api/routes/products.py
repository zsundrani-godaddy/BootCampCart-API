import falcon
from playhouse.shortcuts import model_to_dict
from cart_api.database import DatabaseProducts


class Product:
    def on_get(self, req, resp, product_id):
        product = DatabaseProducts.get(id=product_id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, product_id):
        DatabaseProducts.delete_by_id(product_id)
        resp.status = falcon.HTTP_204


# Excercise 2:
# Products route should respond to GET and POST requests
# GET products returns a list of every product in the database
# POST products creates a product and returns the data it created

        

class Products:
    #pass  # must have a pass line because you cannot have a "blank" class
    def on_get(self, req, resp):
        prod_list = DatabaseProducts.select() 
        res = []

        for prod in prod_list: 
            res.append(model_to_dict(prod))
        
        resp.status = falcon.HTTP_200
        resp.media = res

    def on_post(self, req, resp):
        passobj = req.get_media(req)
        created_record = DatabaseProducts.create(name = passobj["name"], description = ["description"], 
                                    image_url = passobj["image_url"], price = ["price"], 
                                    is_on_sale = passobj["is_on_sale"], sale_price = passobj["sale_price"])
        resp.status = falcon.HTTP_201
        resp.media = model_to_dict(created_record)
