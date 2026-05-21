from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Delivery(models.Model):
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product} -> {self.customer_name} ({self.phone})"