from django.urls import path
from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('add/', ProductCreateView.as_view(), name='product_create'),
]