from django.db import models

from myquote.buyers import Buyer
from myquote.products import Product


# from myquote.seller import Seller

# Create your models here.

class Orders(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=None)
    product = models.ForeignKey(Product, on_delete=None)
    date_for_product = models.DateTimeField(blank=True)
    comment = models.TextField(blank=None)

    def __str__(self):
        return self.buyer
