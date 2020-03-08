from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from .models import Buyer



class BuyersListView(ListView):
    model = Buyer
    template_name = 'buyers.html'


class BuyersCreateView(CreateView):
    model = Buyer
    fields = "__all__"
    template_name = 'create_buyers.html'

    def get_success_url(self):
        return reverse('buyers-list')


class BuyersUpdateView(UpdateView):
    model = Buyer
    fields = "__all__"
    template_name = "update_buyers.html"

    def get_success_url(self):
        return reverse('buyers-list')


class BuyersDeleteView(DeleteView):
    model = Buyer
    template_name = "buyer_confirm_delete.html"
    success_url = reverse_lazy('buyers-list')

