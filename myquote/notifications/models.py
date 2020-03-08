from django.db import models

STATUSES = [
    ('B', 'Buyer'),
    ('S', 'Seller'),
]

class Notification(models.Model):
    type = models.CharField(
        max_length=2,
        choices=STATUSES,
        default='Seller'
    )
    content = models.CharField(max_length=40, default="Buyer")

    @staticmethod
    def load_notifications(request):
        print(" values>> ", Notification.objects.values())
        request.session['notifications'] = list(Notification.objects.values())
