from django.urls import path
from . import views

app_name = 'health_checks'

urlpatterns = [
    path('health/', views.basic_health_check, name='basic-health-check'),
    path('health/db/', views.database_health_check, name='database-health-check'),
    path('health/detailed/', views.detailed_health_check, name='detailed-health-check'),
] 