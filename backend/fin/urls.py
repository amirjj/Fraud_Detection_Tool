from .views import POViewSet, DupAmntSameSupDetailViewSet, DupAmountSameSupViewSet, SplitPOViewSet,\
    SumOfPOPerSupViewSet, POCountPerSupViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'pos', POViewSet, basename='pos')
router.register(r'dupmntsamesupsdetail', DupAmntSameSupDetailViewSet, basename='dupmntsamesupsdetail')
router.register(r'dupmntsamesups', DupAmountSameSupViewSet, basename='dupmntsamesups')
router.register(r'splitpo', SplitPOViewSet, basename='splitpo')
router.register(r'sumofpopersup', SumOfPOPerSupViewSet, basename='sumofpopersup')
router.register(r'pocountpersup', POCountPerSupViewSet, basename='pocountpersup')


urlpatterns = [
    path('', include(router.urls))
]
