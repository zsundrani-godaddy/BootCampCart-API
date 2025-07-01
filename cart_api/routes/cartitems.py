import falcon
from playhouse.shortcuts import model_to_dict

from cart_api.database import DatabaseCartItem


# Exercise 3:
# Using the database model you created in Exercise 1 create a cartitems route
# CartItems should have a responder for POST and GET
# CartItem should have responders for GET DELETE PATCH
# Your API response statuses and bodies should conform to your OpenAPI spec


class CartItems:
    def on_get(self, req, resp):
        cart = DatabaseCartItem.select() 
        res = []

        for item in cart: 
            res.append(model_to_dict(item))
        
        resp.status = falcon.HTTP_200
        resp.media = res

    def on_post(self, req, resp):
        passobj = req.get_media()
        created_record = DatabaseCartItem.create(name = passobj["name"], 
                                                 price = passobj["price"], 
                                                 quantity = passobj["quantity"] )
        resp.status = falcon.HTTP_201
        resp.media = model_to_dict(created_record)
        


class CartItem:
    def on_get(self, req, resp, id):
        product = DatabaseCartItem.get(id = id)
        resp.media = model_to_dict(product)
        resp.status = falcon.HTTP_200
    
    def on_delete(self, req, resp, id):
        DatabaseCartItem.delete_by_id(id)
        resp.status = falcon.HTTP_204
    
    def on_patch(self, req, resp, id): 
        passobj = req.get_media()
        DatabaseCartItem.update(quantity = passobj["quantity"]).where(DatabaseCartItem.id == id).execute()
        resp.status = falcon.HTTP_204
    
    

