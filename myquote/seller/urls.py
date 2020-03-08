from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
from .models import Seller

urlpatterns = [
    path('', sellers_list, name="sellers_list"),
    path('create/', create_seller, name="create_seller"),
    path('<int:id>/', seller, name="seller"),
    path('<int:id_code>/update/', update_seller, name="update_seller"),
    path('<int:id_code>/delete/', delete_seller, name="delete_seller"),
]
