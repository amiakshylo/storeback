import pandas as pd


def verify_data_ids():
    views_df = pd.read_csv('store/recommendations/product_views.csv')
    orders_df = pd.read_csv('store/recommendations/order_items.csv')

    max_user_id_views = views_df['user_id'].max()
    max_user_id_orders = orders_df['order__customer_id'].max()
    max_product_id_views = views_df['product_id'].max()
    max_product_id_orders = orders_df['product_id'].max()

    print(f"Max user ID in views: {max_user_id_views}")
    print(f"Max user ID in orders: {max_user_id_orders}")
    print(f"Max product ID in views: {max_product_id_views}")
    print(f"Max product ID in orders: {max_product_id_orders}")


if __name__ == '__main__':
    verify_data_ids()
