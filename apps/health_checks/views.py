from django.shortcuts import render
from django.db import connections
from django.db.utils import OperationalError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import time


@api_view(['GET'])
@permission_classes([AllowAny])
def basic_health_check(request):
    """
    Health check básico que retorna 200 si el servidor está corriendo.
    """
    return Response({
        'status': 'healthy',
        'timestamp': time.time()
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def database_health_check(request):
    """
    Health check que verifica conectividad con la base de datos.
    """
    try:
        connections['default'].cursor()
        return Response({
            'status': 'healthy',
            'database': 'connected',
            'timestamp': time.time()
        })
    except OperationalError:
        return Response({
            'status': 'unhealthy',
            'database': 'disconnected',
            'timestamp': time.time()
        }, status=status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
@permission_classes([AllowAny])
def detailed_health_check(request):
    """
    Comprehensive health que combina verificación de servidor y base de datos.
    """
    health_status = {
        'status': 'healthy',
        'timestamp': time.time(),
        'checks': {
            'server': 'healthy',
            'database': 'healthy'
        }
    }
    
    # Check database
    try:
        connections['default'].cursor()
    except OperationalError:
        health_status['status'] = 'unhealthy'
        health_status['checks']['database'] = 'unhealthy'
    
    # If any check failed, return 503
    if health_status['status'] == 'unhealthy':
        return Response(health_status, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
    return Response(health_status)
