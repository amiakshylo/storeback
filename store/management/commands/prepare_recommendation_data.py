from django.core.management.base import BaseCommand
from store.models import ProductView, OrderItem
import pandas as pd


class Command(BaseCommand):
    help = 'Prepare data for recommendation system'

    def handle(self, *args, **options):
        views = ProductView.objects.all().values('user_id', 'product_id', 'timestamp')
        views_df = pd.DataFrame(list(views))

        orders = OrderItem.objects.all().values('order__customer_id', 'product_id', 'quantity')
        orders_df = pd.DataFrame(list(orders))

        views_df.to_csv('store/recommendations/product_views.csv', index=False)
        orders_df.to_csv('store/recommendations/order_items.csv', index=False)

        self.stdout.write(self.style.SUCCESS('Data preparation complete'))
