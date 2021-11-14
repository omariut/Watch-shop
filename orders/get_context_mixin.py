from customers.models import Customer
from orders.models import Order, OrderItem, Address

class GetContextMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(customer=self.request.user, complete=False)
        orderitems = order.orderitem_set.all()
        context["orderitems"] = orderitems
        context["order"] = order
        return context