import django_filters

from .models import Product
from django import forms

class ProductFilter(django_filters.FilterSet):
    # status = django_filters.CharFilter(widget=forms.Select(
    #     attrs={
    #     "class":"form-control text-white text-center",
    #     "max_length":"100"
    #     }
    # ))

    class Meta:
        model = Product
        fields = ['status']