
from django.urls import path
from products.views import ProductListView
from customers.views import  CustomerCreateView

app_name ='customers'
urlpatterns = [
    path('create-customer', CustomerCreateView.as_view(), name='create-customer'),
     
  
]
