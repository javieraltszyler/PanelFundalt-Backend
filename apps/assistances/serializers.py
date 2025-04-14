from rest_framework import serializers
from .models import Assistance

class AssistanceSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Assistance
    """
    class Meta:
        model = Assistance
        fields = [
            'id',
            'beneficiary',
            'author',
            'assistance_type',
            'geolocation',
            'address',
            'address_reference',
            'extended_assistance',
            'extended_assistance_details',
            'notes',
            'created_at',
            'updated_at'
        ]
        