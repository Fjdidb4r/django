from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'email', 'phone', 'created_by', 'created_at')
	search_fields = ('name', 'email', 'phone')
