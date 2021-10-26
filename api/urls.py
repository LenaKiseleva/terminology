from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ManualViewSet, RelevantManualViewSet,
                    UnitManualsByManualViewset, UnitManualValidationViewset,
                    UnitManualViewSet)

router_v1 = DefaultRouter()
router_v1.register(
    'manuals',
    ManualViewSet,
    basename='Manual'
)
router_v1.register(
    'units',
    UnitManualViewSet,
    basename='Unit'
)


urlpatterns = [
    path(
        'v1/manuals/relevant/',
        RelevantManualViewSet.as_view({'get': 'list'}),
        name='relevant-manuals',
    ),
    path(
        'v1/manuals/relevant/<str:date>/',
        RelevantManualViewSet.as_view({'get': 'list'}),
        name='relevant-manuals-date',
    ),
    path(
        'v1/units/defined/',
        UnitManualsByManualViewset.as_view({'get': 'list'}),
        name='units-validation',
    ),
    path(
        'v1/units/validation/',
        UnitManualValidationViewset.as_view({'post': 'retrieve'}),
        name='units-validation',
    ),
    path('v1/', include(router_v1.urls)),
]
