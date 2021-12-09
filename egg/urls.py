from .views import EggViewSet
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', EggViewSet)

urlpatterns = [
    path('', include(router.urls))
]
