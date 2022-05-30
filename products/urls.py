from django.urls import path, include
from products.api.view import ProductDetailView, ProductsListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('products', ProductsListView.as_view(), name='products_list'),
    path('product-details/<int:pk>',
         ProductDetailView.as_view(), name='product_details'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]
