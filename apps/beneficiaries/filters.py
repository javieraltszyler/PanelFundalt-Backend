import django_filters
from django.db.models import Q, Func, CharField
from django.db.models.functions import Lower
from .models import Beneficiary


class Unaccent(Func):
    function = 'unaccent'
    output_field = CharField()


class BeneficiaryFilter(django_filters.FilterSet):
    """
    Filtro para el modelo Beneficiary
    """
    search = django_filters.CharFilter(method='filter_search_fields')
    name = django_filters.CharFilter(method='filter_name')
    dni = django_filters.CharFilter(lookup_expr='icontains')

    def filter_search_fields(self, queryset, name, value):
        """
        Búsqueda general que incluye nombre, apellido, apodo y DNI.
        Remueve tildes y convierte a minúsculas para búsqueda flexible.
        """
        value_normalized = value.lower()

        return queryset.annotate(
            first_name_norm=Unaccent(Lower('first_name')),
            last_name_norm=Unaccent(Lower('last_name')),
            nickname_norm=Unaccent(Lower('nickname')),
            dni_norm=Unaccent(Lower('dni'))
        ).filter(
            Q(first_name_norm__icontains=value_normalized) |
            Q(last_name_norm__icontains=value_normalized) |
            Q(nickname_norm__icontains=value_normalized) |
            Q(dni_norm__icontains=value_normalized)
        )

    def filter_name(self, queryset, name, value):
        """
        Filtro específico para nombre que remueve tildes.
        """
        value_normalized = value.lower()

        return queryset.annotate(
            first_name_norm=Unaccent(Lower('first_name')),
            last_name_norm=Unaccent(Lower('last_name'))
        ).filter(
            Q(first_name_norm__icontains=value_normalized) |
            Q(last_name_norm__icontains=value_normalized)
        )

    class Meta:
        model = Beneficiary
        fields = {
            'dni': ['exact', 'icontains'],
            'first_name': ['iexact', 'icontains'],
            'last_name': ['iexact', 'icontains'],
            'nickname': ['iexact', 'icontains'],
        }











# class BeneficiaryFilter(django_filters.FilterSet):
#     """
#     Filtro para el modelo Beneficiary
#     """
#     search = django_filters.CharFilter(method='filter_search_fields')
#     name = django_filters.CharFilter(method='filter_name')
#     dni = django_filters.CharFilter(lookup_expr='icontains')
    
#     def filter_search_fields(self, queryset, name, value):
#         """
#         Búsqueda general que incluye nombre, apellido, apodo y DNI
#         """
#         # Normalizar el valor de búsqueda (remover acentos)
#         # normalized_value = normalize(value)
        
#         return queryset.filter(
#             Q(first_name__icontains=value) |
#             Q(last_name__icontains=value) |
#             Q(nickname__icontains=value) |
#             Q(dni__icontains=value)
#             # Búsqueda normalizada (sin acentos)
#             # Q(first_name__icontains=normalized_value) |
#             # Q(last_name__icontains=normalized_value) |
#             # Q(nickname__icontains=normalized_value)
#         )
    
#     def filter_name(self, queryset, name, value):
#         """
#         Filtro específico para nombre que maneja acentos
#         """
#         # normalized_value = normalize(value)
#         return queryset.filter(
#             Q(first_name__icontains=value) |
#             Q(last_name__icontains=value)
#             # Q(first_name__icontains=normalized_value) |
#             # Q(last_name__icontains=normalized_value)
#         )

#     class Meta:
#         model = Beneficiary
#         fields = {
#             'dni': ['exact', 'icontains'],
#             'first_name': ['iexact', 'icontains'],
#             'last_name': ['iexact', 'icontains'],
#             'nickname': ['iexact', 'icontains'],
#         }