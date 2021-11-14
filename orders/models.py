from django.db import models
from products.models import Product
from customers.models import Customer
from django.urls import reverse
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False)

    @property
    def get_total_price(self):
        item_prices = [item.get_orderitem_price for item in self.orderitem_set.all()]
        total_price = sum(item_prices)
        return total_price
    @property
    def get_total_item(self):
        items = [item.quantity for item in self.orderitem_set.all()]
        total_item = sum(items)
        return total_item

    def get_absolute_url(self):
        return reverse('orders:cart-edit', kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_orderitem_price(self):
        orderitem_price = self.product.unit_price*self.quantity
        return orderitem_price
    def get_absolute_url(self):
        return reverse("orderitem", kwargs={"pk": self.pk})
    
    
 
class Address (models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200,  null=True)
    phone = models.CharField(max_length=200,  null=True)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
    


