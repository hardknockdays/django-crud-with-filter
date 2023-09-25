# -*- coding: utf-8 -*-
from django.db import models

class Kategori(models.Model):
    id_kategori= models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length=100)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('kategori_edit', kwargs={'pk': self.pk})
    
class Status(models.Model):
    id_status= models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length=100)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('status_edit', kwargs={'pk': self.pk})
    
class Product(models.Model):
    id_product= models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', decimal_places=2, max_digits=8)
    kategori = models.ForeignKey(Kategori, on_delete = models.CASCADE)
    status = models.ForeignKey(Status, on_delete = models.CASCADE)
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['id_product']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('product_edit', kwargs={'pk': self.pk})
    
    # def get_absolute_url(self):
    #     return reverse('product_list', kwargs={'pk': self.pk})
    
