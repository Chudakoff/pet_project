from django.shortcuts import render
from django.views.generic import View, TemplateView

# Create your views here.
def index(request):
    return render(request, template_name='app/index.html')

class StartView(TemplateView):
    template_name = 'base.html'