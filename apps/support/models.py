
# apps/support/models.py

from django.db import models
from apps.requests.models import ServiceRequest

class SupportAction(models.Model):
    request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    action_taken = models.TextField()
    action_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Action on {self.request.id}"
