# apps/support/views.py

from django.shortcuts import render
from .models import ServiceRequest, SupportAction

def manage_requests(request):
    requests = ServiceRequest.objects.filter(status='Pending')
    return render(request, 'support/manage_requests.html', {'requests': requests})

