from django.urls import path
from .views import BuyersListView, BuyerCreateView

urlpatterns = [
    path('', BuyersListView.as_view(), name="buyers-list"),
    path('create/', BuyerCreateView.as_view(), name="buyers-create"),
]

