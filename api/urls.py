from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ManualViewSet, UnitManualViewSet

router_v1 = DefaultRouter()
router_v1.register('manuals', ManualViewSet, basename='Manual')
router_v1.register('units', UnitManualViewSet, basename='Unit')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
