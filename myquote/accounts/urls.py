from django.urls import path
from django.views.generic import TemplateView

from .views import user_login, user_logout, user_signup_for_buyers, user_signup_for_seller

urlpatterns = [
    path('login/', user_login, name="user-login"),
    path('logout/', user_logout, name="user-logout"),
    path('signup/', TemplateView.as_view(template_name='seller_buyer_signup_screen.html'), name="user-signup"),
    path('signup/buyer/', user_signup_for_buyers, name="user-signup-buyer"),
    path('signup/seller/', user_signup_for_seller, name="user-signup-seller"),
]

