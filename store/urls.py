from cgitb import lookup

from django.urls import include, path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductVievSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('customers', views.CustomerViewSet)
router.register('reviews', views.ReviewViewSet, basename='reviews')
router.register('orders', views.OrderViewSet, basename='orders')


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

customers_router = routers.NestedDefaultRouter(router, 'customers', lookup='customer')
customers_router.register('orders', views.OrderViewSet, basename='customer-order')

#URLConf
urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('', include(customers_router.urls))
]

