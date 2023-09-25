# -*- coding: utf-8 -*-
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        
        self.fields['price'].widget.attrs = {
            'class': 'form-control col-md-6',
            'step': 'any',
            'min': '1',
        }
        
        self.fields['kategori'].widget.attrs = {
            'class': 'form-control col-md-6'
        }
        
        self.fields['status'].widget.attrs = {
            'class': 'form-control col-md-6'
        }

    class Meta:
        model = Product
        fields = ('name', 'price', 'kategori', 'status')