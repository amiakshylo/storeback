from cgitb import lookup

from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductVievSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('customers', views.CustomerViewSet)


products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls

