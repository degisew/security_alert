from django.urls import path

from core.views import produce


urlpatterns = [
    path('security-alerts/', produce, name='alert'),
]