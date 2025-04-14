import django_filters
from .models import Assistance
from rest_framework import filters


class AssistanceFilter(django_filters.FilterSet):
    """
    Filtro para el modelo Assistance
    """
    class Meta:
        model = Assistance
        fields = {
            'created_at': ['iexact', 'icontains'],
            'assistance_type': ['iexact', 'icontains'],
        }