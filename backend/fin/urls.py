from .views import POViewSet, DupAmntSameSupViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pos', POViewSet, basename='pos')
router.register(r'dupmntsamesups', DupAmntSameSupViewSet, basename='dupamntsamesups')


urlpatterns = [
    path('', include(router.urls))
]
