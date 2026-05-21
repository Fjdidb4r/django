from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer


# def customer_list(request):
#     customers = Customer.objects.all()
#     return render(request, 'customer/list.html', {'customers': customers})


class CustomerListView(LoginRequiredMixin, ListView):
	model = Customer
	template_name = 'customer/list.html'
	context_object_name = 'customers'


class CustomerCreateView(LoginRequiredMixin, CreateView):
	model = Customer
	fields = ['name', 'email', 'phone', 'address']
	template_name = 'customer/add.html'
	success_url = reverse_lazy('customer_list')

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
	model = Customer
	fields = ['name', 'email', 'phone', 'address']
	template_name = 'customer/update.html'
	success_url = reverse_lazy('customer_list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
	model = Customer
	template_name = 'customer/delete.html'
	success_url = reverse_lazy('customer_list')
