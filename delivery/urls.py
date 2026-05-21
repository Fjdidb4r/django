from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeliveryListView.as_view(), name='delivery_list'),
    path('add/', views.DeliveryCreateView.as_view(), name='delivery_add'),
    path('update/<int:pk>/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    path('delete/<int:pk>/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('api/deliveries/', views.DeliveryListCreateAPI.as_view(), name='api_delivery_list'),
    path('api/delivery/', views.DeliveryListCreateAPI.as_view(), name='api_delivery_list_singular'),
]
