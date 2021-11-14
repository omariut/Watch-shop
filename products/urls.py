
from django.urls import path
from products.views import ProductListView


urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
     
  
]
