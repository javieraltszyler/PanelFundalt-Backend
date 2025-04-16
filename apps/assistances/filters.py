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















# import django_filters
# from django.db.models import Q
# from .models import Assistance

# class AssistanceFilter(django_filters.FilterSet):
#     """
#     Filtro para el modelo Assistance
#     """
#     search = django_filters.CharFilter(method='filter_search_fields')
#     created_at = django_filters.DateFilter()
    
#     def filter_search_fields(self, queryset, name, value):
#         """
#         Búsqueda general que incluye fecha de creación, tipo de asistencia,
#         autor y beneficiario
#         """
#         return queryset.filter(
#             Q(created_at__icontains=value) |
#             Q(assistance_type__icontains=value) |
#             Q(author__first_name__icontains=value) |
#             Q(author__last_name__icontains=value) |
#             Q(beneficiary__first_name__icontains=value) |
#             Q(beneficiary__last_name__icontains=value) |
#             Q(beneficiary__nickname__icontains=value) |
#             Q(beneficiary__dni__icontains=value)
#         )

#     class Meta:
#         model = Assistance
#         fields = {
#             'created_at': ['exact', 'icontains', 'gte', 'lte'],
#             'assistance_type': ['exact', 'icontains'],
#             'author': ['exact'],
#             'beneficiary': ['exact'],
#         }