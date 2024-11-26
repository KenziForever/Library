
from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from django.views import generic
from django.shortcuts import get_object_or_404, redirect



class OrderListView(generic.ListView):
    template_name = 'order_list.html'
    context_object_name = 'orders'
    model = Order

    def get_queryset(self):
        return Order.objects.all()


class CreateOrderView(generic.CreateView):
    form_class = OrderForm
    template_name = 'create_order.html'
    success_url = '/basket/orders/'

    def form_valid(self, form):
        return redirect('order_list')


class DeleteOrderView(generic.DeleteView):
    template_name = 'delete_order.html'
    success_url = '/basket/orders/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)

    def form_valid(self, form):
        return redirect('order_list')


class UpdateOrderView(generic.UpdateView):
    form_class = OrderForm
    template_name = 'update_order.html'
    success_url = '/basket/orders/'

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)

    def form_valid(self, form):
        return redirect('order_list')


class OrderDetailView(generic.DetailView):
    template_name = 'order_detail.html'
    context_object_name = 'order'
    model = Order

    def get_object(self, **kwargs):
        order_id = self.kwargs.get('id')
        return get_object_or_404(Order, id=order_id)
