from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
   
    success_url = reverse_lazy('accounts:login')


class HomeView(TemplateView):
   
    template_name = 'base.html'


def logout_view(request):
   
    logout(request)
    return redirect('accounts:login')