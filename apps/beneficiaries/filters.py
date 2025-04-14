import django_filters
from django.db.models import Q
from .models import Beneficiary
# from django.utils.text import normalize


class BeneficiaryFilter(django_filters.FilterSet):
    """
    Filtro para el modelo Beneficiary
    """
    search = django_filters.CharFilter(method='filter_search_fields')
    name = django_filters.CharFilter(method='filter_name')
    dni = django_filters.CharFilter(lookup_expr='icontains')
    
    def filter_search_fields(self, queryset, name, value):
        """
        Búsqueda general que incluye nombre, apellido, apodo y DNI
        """
        # Normalizar el valor de búsqueda (remover acentos)
        # normalized_value = normalize(value)
        
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value) |
            Q(nickname__icontains=value) |
            Q(dni__icontains=value)
            # Búsqueda normalizada (sin acentos)
            # Q(first_name__icontains=normalized_value) |
            # Q(last_name__icontains=normalized_value) |
            # Q(nickname__icontains=normalized_value)
        )
    
    def filter_name(self, queryset, name, value):
        """
        Filtro específico para nombre que maneja acentos
        """
        # normalized_value = normalize(value)
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
            # Q(first_name__icontains=normalized_value) |
            # Q(last_name__icontains=normalized_value)
        )

    class Meta:
        model = Beneficiary
        fields = {
            'dni': ['exact', 'icontains'],
            'first_name': ['iexact', 'icontains'],
            'last_name': ['iexact', 'icontains'],
            'nickname': ['iexact', 'icontains'],
        }