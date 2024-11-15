
# apps/requests/models.py

from django.db import models
from apps.accounts.models import UserProfile

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]
    
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Request #{self.id} - {self.request_type}"
