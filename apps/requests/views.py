# apps/requests/views.py

from django.shortcuts import render
from .forms import ServiceRequestForm
from .models import ServiceRequest

def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'requests/create_request.html', {'form': form})

def track_request(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.profile)
    return render(request, 'requests/track_request.html', {'requests': service_requests})

