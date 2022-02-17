from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import StatesViewSet

router = DefaultRouter()

router.register("state", StatesViewSet, basename="state")

urlpatterns = [
    path("", include(router.urls)),
]
