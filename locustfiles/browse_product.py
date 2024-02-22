
import random
from locust import HttpUser, task, between


class WebUser(HttpUser):
    wait_time = between(1, 6)
    
    @task(2)
    def view_products(self):
        collection_id = random.randint(2, 6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name='/store/products/')
    
    @task(4)    
    def view_product(self):
        product_id = random.randint(1, 1000)
        self.client.get(f'/store/products/{product_id}/', name='/store/products/:id')
        
    @task(1)
    def add_product_to_cart(self):
        product_id = random.randint(1, 10)
        quantity = 1
        self.client.post('/store/carts/632195a6-68ac-4986-ad2e-e02080dbfff5/items/', name='/store/cart/items/', data={
            'product_id': product_id,
            'quantity': quantity
        })
    
    @task    
    def say_hello(self):
        self.client.get('/playground/hello/')
    # def on_start(self):
    #     response = self.client.post('/store/carts/')
    #     result = response.json()
    #     print(result)
        # self.cart_id = result['id']
        
    