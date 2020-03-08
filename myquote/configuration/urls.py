from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import (TeamMemberView)

urlpatterns = [
    path('', login_required(TeamMemberView.as_view()), name="team-members"),
]