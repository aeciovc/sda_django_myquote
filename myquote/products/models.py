from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)





