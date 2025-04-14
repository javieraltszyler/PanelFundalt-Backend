from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

app_name = 'assistances'

urlpatterns = []

router = DefaultRouter()
router.register('', views.AssistanceViewSet)
urlpatterns += router.urls 