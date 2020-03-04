from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView)
from .models import Buyer
from .forms import ContactForm


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


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thank_you')
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})