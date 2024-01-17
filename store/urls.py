from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductVievSet)
router.register('collections', views.CollectionViewSet)
router.register('customers', views.CustomerViewSet)
router.register('reviews', views.ReviewViewSet)

# URLConf
urlpatterns = router.urls
# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),  # """aply converter to parametr 'id', int: """
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection-detail'),
#     path('collections/', views.CollectionList.as_view()),
#     path('customers/', views.CustomerList.as_view()),
#     path('customers/<int:pk>/', views.CustomerDetail.as_view())
# ]
