from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('buyers-list'))
            else:
                return HttpResponse("Your account was inactive.")
        else:

            return HttpResponse("Invalid login details given. Go back and try again")
    else:
        return render(request, 'login.html', {})
