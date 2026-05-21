from django.contrib import admin
from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
	list_display = ('id', 'product', 'customer_name', 'phone', 'created_by', 'created_at')
	search_fields = ('customer_name', 'product', 'phone', 'address')
	list_filter = ('created_by',)
