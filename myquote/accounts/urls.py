from django.urls import path

from .views import user_login, user_logout, user_signup_for_buyers

urlpatterns = [
    path('login/', user_login, name="user-login"),
    path('logout/', user_logout, name="user-logout"),
    path('signup/buyer', user_signup_for_buyers, name="user-signup-buyer"),
]

