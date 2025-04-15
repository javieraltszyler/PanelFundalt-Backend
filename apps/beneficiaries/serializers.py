from rest_framework import serializers
from .models import Beneficiary


class BeneficiarySerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Beneficiary
    """
    class Meta:
        model = Beneficiary
        fields = [
            'id',
            'dni',
            'author',
            'author_details',
            'has_physical_dni',
            'first_name',
            'last_name',
            'nickname',
            'birthdate',
            'phone_number',
            'reference_phone_number',
            'geolocation',
            'address',
            'address_reference',
            'sex',
            'nationality',
            'is_fixed_or_transitory_place',
            'life_center',
            'has_family_contact',
            'subsidies',
            'subsidies_details',
            'health_info'
        ]


# Read only > id, etc