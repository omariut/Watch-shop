from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "main/home.html"