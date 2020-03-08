from django.db import models


class Seller(models.Model):
    # Needed fields: name, email, id_code, phonenumber, dt_entrance
    id_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone_number = models.BigIntegerField(unique=True)
    dt_entrance = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.id_code)
