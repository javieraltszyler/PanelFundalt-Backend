from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Assistance
from .serializers import AssistanceSerializer
from .filters import AssistanceFilter

class AssistanceViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar las asistencias
    """
    queryset = Assistance.objects.all()
    serializer_class = AssistanceSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None #Cambiar a PageNumberPagination en el futuro 
    filterset_class = AssistanceFilter
    filter_backends = [DjangoFilterBackend]
    search_fields = ['assistance_type', 'created_at']








