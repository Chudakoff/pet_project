from django.urls import path, include
from .views import index, StartView, ProductListView, ProductCreateView

urlpatterns = [
   path('', index, name='index'),
   path('base/', StartView.as_view(), name='start'),
   path('product/', ProductListView.as_view(), name='products'),
   path('product/create/', ProductCreateView.as_view(), name='create'),
]