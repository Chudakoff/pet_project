from .models import Product
from django.forms import ModelForm

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'