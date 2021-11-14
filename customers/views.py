from django.shortcuts import render
from customers.models import Customer
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from customers.forms import CustomerCreationForm, CustomerChangeForm
from django.urls import reverse_lazy
# Create your views here.

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('orders:add-to-cart')



