from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (BuyersListView, BuyersCreateView, BuyersUpdateView, BuyersDeleteView)

urlpatterns = [
    path('', login_required(BuyersListView.as_view()), name="buyers-list"),
    path('create/', login_required(BuyersCreateView.as_view()), name="buyers-create"),
    path('update/<int:pk>/', login_required(BuyersUpdateView.as_view()), name="buyers-update"),
    path('delete/<int:pk>/', login_required(BuyersDeleteView.as_view()), name="buyers-delete"),

]

