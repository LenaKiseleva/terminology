from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Manual, UnitManual
from .permissions import IsAdminUserOrReadOnly
from .serializers import ManualSerializer, UnitManualListSerializer


class ManualViewSet(ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'short_name',
                        'commencement_date', 'version']
    search_fields = ['id', 'name', 'short_name', 'description',
                     'version', 'commencement_date']
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination


class UnitManualViewSet(ModelViewSet):
    queryset = UnitManual.objects.all()
    serializer_class = UnitManualListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'manual', 'code_unit', 'value_unit', ]
    search_fields = ['id', 'manual', 'code_unit', 'value_unit', ]
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination
