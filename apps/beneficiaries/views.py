from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Beneficiary
from .serializers import BeneficiarySerializer
from .filters import BeneficiaryFilter


class BeneficiaryViewSet(viewsets.ModelViewSet):
    """
    Vista para gestionar los beneficiarios
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = None
    filterset_class = BeneficiaryFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'nickname', 'dni']


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_serializer_class(self):
    # # can also check if POST: if self.request.method == 'POST'
    #     if self.action == 'create' or self.action == 'update':
    #         return OrderCreateSerializer
    #     return super().get_serializer_class()

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     if not self.request.user.is_staff:
    #         qs = qs.filter(user=self.request.user)
    #     return qs