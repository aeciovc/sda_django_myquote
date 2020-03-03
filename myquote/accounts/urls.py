from django.urls import path

from .views import user_login, user_logout

urlpatterns = [
    path('login/', user_login, name="user-login"),
    path('logout/', user_logout, name="user-logout"),
]

