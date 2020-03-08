from django.views.generic import (ListView)
from .models import TeamMember

# Create your views here.
class TeamMemberView(ListView):
    model = TeamMember
    template_name = 'aboutt.html'
