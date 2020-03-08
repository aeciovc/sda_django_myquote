from django.contrib.auth.models import User
from django.db import models


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
    id_code = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.BigIntegerField(unique=True)
    dt_entrance = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.user, self.id_code)

