from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic import DetailView, TemplateView
from products.models import Product
from customers.models import Customer
from orders.models import Order, OrderItem, Address
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from orders.get_context_mixin import GetContextMixin


class CreateOrderItem(GetContextMixin, CreateView):
    model = OrderItem
    fields = ["product"]
    template_name = "home.html"
    success_url = reverse_lazy("orders:add-to-cart")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        order = super().get_current_order()
        orderitems = order.orderitem_set.all()
        products_in_order = [orderitem.product for orderitem in orderitems]
        context["products_in_order"] = products_in_order
        context["order"] = order
        return context

    def form_valid(self, form):
        product = form.instance.product
        order = super().get_current_order()
        orderitem, created = OrderItem.objects.get_or_create(
            order=order, product=product
        )
        orderitem.quantity = 1
        form.instance = orderitem
        return super().form_valid(form)


class EditCart(UpdateView):
    model = Order
    template_name = "cart.html"
    success_url = reverse_lazy("orders:add-to-cart")

    def get_form_class(self):
        formset = inlineformset_factory(
            Order,
            OrderItem,
            fields=("quantity",),
            extra=0,
        )
        form_class = formset
        return form_class

    def form_valid(self, form):
        form.save()
        print(self.success_url)
        return redirect("orders:checkout")


class CheckOutView(GetContextMixin, CreateView):
    model = Address
    fields = "__all__"
    template_name = "checkout.html"
    success_url = reverse_lazy("orders:confirmation")


class ConfirmationView(TemplateView):
    template_name = "confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            order = Order.objects.get(customer=self.request.user, complete=False)
        except:
            id = self.request.session["order_id"]
            order = Order.objects.get(id=id)
        context["order"] = order
        orderitems = order.orderitem_set.all()
        context["orderitems"] = orderitems
        return context
