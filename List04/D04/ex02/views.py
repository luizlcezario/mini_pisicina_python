from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm
from django.urls import reverse
from django.conf import settings
import os
from datetime import datetime

# Create your views here.
def index(request):
    if (request.method == "POST"):
        form = MyForm(request.POST)
        if (form.is_valid()):
            log = f"{datetime.now()} | {form.cleaned_data['campo']}\n"
            with open(settings.LOG_FILE, 'a') as f:
                f.write(log)
            return HttpResponseRedirect(reverse("ex02:index"))

    form = MyForm()
    if os.path.isfile(settings.LOG_FILE) == True: 
        with open(settings.LOG_FILE, 'r') as f:
            file = f.readlines()
    else:
        file = []
    return render(request, "ex02/form.html",{
        'form': form, 'history_file': list(reversed(file))
    })
