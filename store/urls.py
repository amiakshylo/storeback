from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),  # """aply converter to parametr 'id', int: """
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
    path('collections/', views.CollectionList.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetail.as_view())
]
