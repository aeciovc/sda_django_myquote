from django.db import models
from django.utils import timezone

STATUSES = [
    ('P', 'Published'),
    ('NP', 'Not published'),
]


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=200, default="system")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200, default='N/A')
    status = models.CharField(
        max_length=2,
        choices=STATUSES,
        default='NP'
    )
    image = models.ImageField(default='default_image.jpg', upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name





