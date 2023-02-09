from django.shortcuts import render
from django.views.generic import TemplateView

class Djangoview(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'name': 'django'
        }
        return render(request, 'django.html', context) 

class Displayview(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'name': 'display'
        }
        return render(request, 'display.html', context) 

class Templatesview(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'name': 'templates'
        }
        return render(request, 'templates.html', context) 