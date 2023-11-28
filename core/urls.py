from django.urls import path

from core.views import produce


urlpatterns = [
    path('produce/', produce, name='produce'),
]