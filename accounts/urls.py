from django.urls import path
from django.urls import reverse_lazy
from .views import CustomLoginView, RegisterView, logout_view

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
   
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
