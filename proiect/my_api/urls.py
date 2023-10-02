from rest_framework import routers
from django.urls import path, include
from my_api import views

router = routers.DefaultRouter()
router.register('api2', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls))
]
