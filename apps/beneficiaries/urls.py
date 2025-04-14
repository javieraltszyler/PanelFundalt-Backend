from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

app_name = 'beneficiaries'

urlpatterns = []

router = DefaultRouter()
router.register('', views.BeneficiaryViewSet)
urlpatterns += router.urls 