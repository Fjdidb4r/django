from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Delivery

from rest_framework.generics import ListCreateAPIView
from .serializers import DeliverySerializer


# def delivery_list(request):
#     deliveries = Delivery.objects.all()
#     return render(request, 'delivery/delivery.html', {'deliveries': deliveries})


# def delivery_create(request):
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery')
#     else:
#         form = DeliveryForm()
#     return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'Add Delivery'})


# def delivery_update(request, pk):
#     obj = get_object_or_404(Delivery, pk=pk)
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST, instance=obj)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery')
#     else:
#         form = DeliveryForm(instance=obj)
#     return render(request, 'delivery/delivery_form.html', {'form': form, 'title': 'Edit Delivery'})


# def delivery_delete(request, pk):
#     obj = get_object_or_404(Delivery, pk=pk)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('delivery')
#     return render(request, 'delivery/delivery_confirm_delete.html', {'object': obj})

class DeliveryListView(LoginRequiredMixin, ListView):
    model = Delivery
    template_name = 'delivery/list.html'
    context_object_name = 'deliveries'


class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Delivery
    fields = ['customer_name', 'address', 'phone', 'product']
    template_name = 'delivery/add.html'
    success_url = reverse_lazy('delivery_list')

    def form_valid(self, form):
       
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DeliveryUpdateView(LoginRequiredMixin, UpdateView):

    model = Delivery
    fields = ['customer_name', 'address', 'phone', 'product']
    template_name = 'delivery/update.html'
    success_url = reverse_lazy('delivery_list')



class DeliveryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
   
    permission_required = 'delivery.delete_delivery'
    model = Delivery
    template_name = 'delivery/delete.html'
    success_url = reverse_lazy('delivery_list')


class DeliveryListCreateAPI(ListCreateAPIView):
      

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer