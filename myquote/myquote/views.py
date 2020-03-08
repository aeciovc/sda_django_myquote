from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'thank_you.html', {'data': form.cleaned_data})
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
