from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField(unique=True)
    id_code = models.CharField(max_length=50)
    dt_entrance = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.id_code)

