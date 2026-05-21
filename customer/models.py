from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
	"""Simple customer model used by the app."""
	name = models.CharField(max_length=120)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=30, blank=True)
	address = models.TextField(blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.phone})"
