# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('requests/', include('apps.requests.urls')),
    path('support/', include('apps.support.urls')),
]

