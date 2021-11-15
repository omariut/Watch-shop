from customers.models import Customer
from orders.models import Order, OrderItem, Address


class GetContextMixin:
    def get_current_order(self):
        try:
            order = Order.objects.get_or_create(
                customer=self.request.user, complete=False
            )
        except:
            try:
                id = self.request.session["order_id"]
                order = Order.objects.get(id=id)
            except:
                order = Order.objects.create(complete=False)
                self.request.session["order_id"] = order.id
        return order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_current_order()
        orderitems = order.orderitem_set.all()
        context["orderitems"] = orderitems
        context["order"] = order
        return context
