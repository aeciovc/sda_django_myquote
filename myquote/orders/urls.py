from django.urls import path
from .views import OrderView

urlpatterns = [
    # path('', product_list, name='products_list')
    # path('', ProductListView.as_view(), name='products_list'),
    path('buy-products/', OrderView.as_view(), name='buy_products')
]
