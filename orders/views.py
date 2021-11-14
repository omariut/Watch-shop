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

# Create your views here

class CreateOrderItem(CreateView):
    model = OrderItem
    fields = ['product']
    template_name = 'home.html'
    success_url = reverse_lazy('orders:add-to-cart')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        if user.is_authenticated: 
            order, created = Order.objects.get_or_create(customer = self.request.user, complete=False )
            orderitems = order.orderitem_set.all()
            products_in_order = [orderitem.product for  orderitem in orderitems]
            context['products_in_order'] =  products_in_order
            context['order'] = order
        return context
    
    def form_valid(self, form):
        product = form.instance.product
        order,created = Order.objects.get_or_create(customer = self.request.user, complete=False )
        orderitem,created = OrderItem.objects.get_or_create(order=order, product=product)
        orderitem.quantity = 1
        form.instance = orderitem
        return super().form_valid(form)


class EditCart(UpdateView):
    model = Order
    template_name = 'cart.html'
    success_url = reverse_lazy('orders:add-to-cart')
    
    def get_form_class(self):
        formset = inlineformset_factory(
            Order, OrderItem, 
            fields=('quantity',), 
            extra=0,
            )
        form_class = formset
        return form_class
    
    def form_valid(self, form):
        form.save()
        print(self.success_url)
        return redirect('orders:checkout')

class CheckOutView(GetContextMixin,CreateView ):
    model = Address
    fields = '__all__'
    template_name = 'checkout.html'
    success_url = reverse_lazy('orders:confirmation')

    def form_valid(self, form):
        
        return super().form_valid(form)

class ConfirmationView(GetContextMixin, TemplateView):
    template_name='confirmation.html'

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(customer=self.request.user, complete=False)
        order.complete = True
        order.save()
        return super().post(request, *args, **kwargs)







    



    

    




    
    




def create_or_update_orderitem (request):
    if request.method == 'POST':
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        print(quantity)
    product = Product.objects.get(id=product_id)
    customer,created = Customer.objects.get_or_create (user=request.user)
    order,created = Order.objects.get_or_create(customer = customer )
    orderitem,created = OrderItem.objects.get_or_create(order=order, product=product)
    orderitem.quantity = quantity
    orderitem.save()
    data = order.get_total_item
    return JsonResponse(data,safe=False)



    def get_cart_total(request):

        total_item = 0

        if user.is_authenticated:
            customer = Customer.objects.get (user=request.user)
            order= Order.objects.get(customer = customer )
            orderitem = OrderItem.objects.get(order=order)
            for item in orderitem:
                total_item += item.quantity
            return total_item

        else:
            for name,quantity in request.session.items():
                try:
            
                    product = Product.objects.get(name = name )
                    total_price += product.unit_price * quantity
                    return total_price 
                except:
                    pass
