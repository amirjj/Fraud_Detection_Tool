from .views import POViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pos', POViewSet)

urlpatterns = [
    path("", include(router.urls))
]
