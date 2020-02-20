from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView
from .models import Buyer


class BuyersListView(ListView):
    model = Buyer
    template_name = 'buyers.html'


class BuyerCreateView(CreateView):
    model = Buyer
    fields = "__all__"
    template_name = 'create_buyers.html'

    def get_success_url(self):
        return reverse('buyers-list')
