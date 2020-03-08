from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    picture = models.ImageField(default='default_image.jpg', upload_to='product_images/')