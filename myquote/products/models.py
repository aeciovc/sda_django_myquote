from django.db import models

STATUSES = [
    ('P', 'Published'),
    ('NP', 'Not published'),
]


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.CharField(max_length=200)
    status = models.CharField(
        max_length=2,
        choices=STATUSES,
        default='NP'
    )
    image = models.ImageField(default='default_image.jpg', storage='product_image')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)





