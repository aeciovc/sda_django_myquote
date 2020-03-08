from django.views.generic import ListView
from .models import Notification

class NotificationListView(ListView):
    model = Notification
    template_name = 'notifications_list.html'
    context_object_name = 'notifications'




