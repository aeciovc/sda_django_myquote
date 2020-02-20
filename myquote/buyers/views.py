from django.shortcuts import render
from django.views.generic import ListView
from .models import Buyer


class BuyersListView(ListView):

    model = Buyer
    template_name = 'buyers.html'

