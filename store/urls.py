from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),  # """aply converter to parametr 'id', int: """
    path('collections/<int:id>/', views.collection_detail, name='collection-detail'),
    path('collections/', views.collection_list),
    path('customers/', views.customer_list),
    path('customers/<int:id>/', views.customer_detail)
]
