from django.urls import path, include
from .views import index, StartView

urlpatterns = [
   path('', index, name='index'),
   path('base/', StartView.as_view(), name='start'),
]