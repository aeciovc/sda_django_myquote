from django.urls import path
from .views import (BuyersListView, BuyersCreateView,
                    BuyersUpdateView, BuyersDeleteView)

urlpatterns = [
    path('', BuyersListView.as_view(), name="buyers-list"),
    path('create/', BuyersCreateView.as_view(), name="buyers-create"),
    path('update/<int:pk>/', BuyersUpdateView.as_view(), name="buyers-update"),
    path('delete/<int:pk>/', BuyersDeleteView.as_view(), name="buyers-delete"),

]
