from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Device, Category, Feature
from .forms import DeviceForm


class DeviceListView(generic.ListView):
    template_name = "device_list.html"
    context_object_name = "devices"
    model = Device

    def get_queryset(self):
        category_filter = self.request.GET.get('category')
        if category_filter:
            return Device.objects.filter(category__name=category_filter)
        return Device.objects.all()


class DeviceDetailView(generic.DetailView):
    template_name = "device_detail.html"
    context_object_name = "device"
    model = Device

    def get_object(self):
        device_id = self.kwargs.get("pk")
        return get_object_or_404(Device, pk=device_id)


class DeviceCreateView(generic.CreateView):
    model = Device
    form_class = DeviceForm
    template_name = "add_device.html"
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect('device_list')


class DeviceUpdateView(generic.UpdateView):
    model = Device
    form_class = DeviceForm
    template_name = "edit_device.html"
    success_url = '/'

    def get_object(self):
        device_id = self.kwargs.get("pk")
        return get_object_or_404(Device, pk=device_id)


class DeviceDeleteView(generic.DeleteView):
    model = Device
    template_name = "delete_device.html"
    success_url = '/'

    def get_object(self):
        device_id = self.kwargs.get("pk")
        return get_object_or_404(Device, pk=device_id)
