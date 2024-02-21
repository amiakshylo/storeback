
import random
from locust import HttpUser, task, between


class WebUser(HttpUser):
    wait_time = between(1, 6)
    
    @task(2)
    def view_products(self):
        collection_id = random.randint(2, 6)
        self.client.get(f'store/products/?collection_id={collection_id}')
    
    @task(4)    
    def view_product(self):
        product_id = random.randint(1, 1000)
        self.client.get(f'store/products/{product_id}/')
        
    @task(1)
    def add_product_to_cart(self):
        product_id = random.randint(1, 10)
        quantity = 1
        self.client.post(f'store/carts/{self.cart_id}/items', data={
            'product_id': product_id,
            'quantity': quantity
        })
        
    def on_start(self):
        response = self.client.post('store/carts/')
        result = response.json()
        self.cart_id = result['id']
        
    