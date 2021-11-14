
from django.urls import path
from orders.views import CreateOrderItem, EditCart, CheckOutView, ConfirmationView

app_name = 'orders'

urlpatterns = [
    path('add-to-cart/', CreateOrderItem.as_view(), name='add-to-cart'),
    path('cart-edit/<int:pk>', EditCart.as_view(), name='cart-edit'),
    path('checkout', CheckOutView.as_view(), name='checkout'),
    path('confirmation', ConfirmationView.as_view(), name ='confirmation'),
  


     
  
]
