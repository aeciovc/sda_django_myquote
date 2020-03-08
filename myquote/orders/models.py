from django.db import models


from buyers.models import Buyer
from products.models import Product
from seller.models import Seller


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    date_for_product = models.DateTimeField(blank=None, default=None)
    quantity = models.TextField(blank=False, default=None)
    comment = models.TextField(blank=None)

    def __str__(self):
        return self.buyer
