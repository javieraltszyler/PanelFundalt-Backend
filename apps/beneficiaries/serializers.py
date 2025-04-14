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
            'first_name',
            'last_name',
            'nickname',
            'birthdate',
            'phone_number',
            'reference_phone_number',
            'location',
            'is_fixed_or_transitory_place',
            'contact_info',
            'life_center',
            'receives_subsidies',
            'subsidies_details',
            'health_info'
        ]


# Read only > id, etc