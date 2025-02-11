from django.urls import path
from .views import employee_stats

urlpatterns = [
    path('stats/', employee_stats, name='employee-stats'),
]
