from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView


from .forms import CreateOrder
from .models import Order
from django.views.generic import CreateView


# Create your views here.

class OrderView(CreateView):
    model = Order
    template_name = 'buy_product.html'
    form_class = CreateOrder






# class ProductListView(ListView):
#     model = Product
#     template_name = 'buy_product.html'
#     context_object_name = 'products'
#

# def product_list(request):
#     model = Product.object.all()
#     return render(request, 'products_list', {'products': model})
# @csrf_exempt
# def buy_product(request):
#     if request.method == 'GET':
#         model = Product
#         return render(request, 'buy_product.html', {'products': model})
#     else:
#         orders = Orders(product=request.POST('product'),
#                         date_for_product=request.POST('time')
#                         )
#         orders.save()
#         return render(request, 'buy_product.html')
