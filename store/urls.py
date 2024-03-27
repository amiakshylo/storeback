from django.urls import include, path
from store import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("products", views.ProductViewSet, basename="products")
router.register("collections", views.CollectionViewSet, basename="collections")
router.register("customers", views.CustomerViewSet)
router.register("reviews", views.ReviewViewSet, basename="reviews")
router.register("orders", views.OrderViewSet, basename="orders")
router.register("carts", views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

collections_router = routers.NestedDefaultRouter(router, "collections", lookup="collection")
collections_router.register(    "products", views.ProductViewSet, basename="collection-product")

customers_router = routers.NestedDefaultRouter(router, "customers", lookup="customer")
customers_router.register("orders", views.OrderViewSet, basename="customer-order")

cart_router = routers.NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")

image_router = routers.NestedDefaultRouter(router, "products", lookup="product")
image_router.register("images", views.ProductImageViewSet, basename="product_images")

address_router = routers.NestedDefaultRouter(router, "customers", lookup="customer")
address_router.register("addresses", views.AddressViewSet, basename="customer_address")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls)),
    path("", include(customers_router.urls)),
    path("", include(collections_router.urls)),
    path("", include(cart_router.urls)),
    path("", include(image_router.urls)),
    path("", include(address_router.urls)),
]
