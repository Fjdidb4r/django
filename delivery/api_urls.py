from django.urls import path
from .views import DeliveryListCreateAPI

urlpatterns = [
    path('deliveries/', DeliveryListCreateAPI.as_view(), name='api_delivery_list'),
    path('delivery/', DeliveryListCreateAPI.as_view(), name='api_delivery_list_singular'),
]
