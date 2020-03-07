from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailView, CategoryDeleteView
from .views import ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='products_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('add/', ProductCreateView.as_view(), name='product_create'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete')
]
