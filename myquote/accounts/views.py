from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from buyers.models import Buyer
from .forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in :)")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('buyers-list'))
            else:
                return HttpResponse("Your account is inactive.")
        else:

            return HttpResponse("Invalid login details given. Go back and try again")
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)

    return redirect('index')


def user_signup_for_buyers(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            our_user = User.objects.get(username=username)
            phone_number = form.cleaned_data.get('phone')
            id_code = form.cleaned_data.get('id_code')
            dt_entrance = form.cleaned_data.get('dt_entrance')
            buyer_profile = Buyer(user=our_user, phone_number=phone_number, id_code=id_code, dt_entrance=dt_entrance)
            buyer_profile.save()

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
