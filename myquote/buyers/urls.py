from django.urls import path
from .views import BuyersListView

urlpatterns = [
    path('', BuyersListView.as_view(), name="buyers-list")
]

