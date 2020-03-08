from django.db import models

STATUSES = [
    ('B', 'Buyer'),
    ('S', 'Seller'),
]

class notifications(models.Model):
    type = models.CharField(
        max_length=2,
        choices=STATUSES,
        default='B'
    )