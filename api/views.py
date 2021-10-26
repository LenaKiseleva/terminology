from datetime import date as current_date
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Manual, UnitManual
from .permissions import IsAdminUserOrReadOnly
from .serializers import ManualSerializer, UnitManualSerializer


class ManualViewSet(ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'version']
    search_fields = ['id', 'name', 'version']
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination


class UnitManualViewSet(ModelViewSet):
    queryset = UnitManual.objects.all()
    serializer_class = UnitManualSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['id', 'manual', 'code_unit', 'value_unit', ]
    search_fields = ['id', 'manual', 'code_unit', 'value_unit', ]
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = PageNumberPagination


class RelevantManualViewSet(ModelViewSet):
    """ Отдает список справочников, актуальных на указанную дату."""
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
    filterset_fields = ['id', 'date_expiration', 'date_commencement', ]
    search_fields = ['id', 'date_expiration', 'date_commencement', ]

    def get_queryset(self):
        manuals = Manual.objects.all()
        date = self.request.parser_context['kwargs'].get('date')
        if date is not None:
            date = datetime.strptime(date, '%Y-%m-%d')
        else:
            date = current_date.today()
        manuals = manuals.filter(
            date_commencement__lte=date,
            date_expiration__gt=date,
        )
        return manuals


class UnitManualsByManualViewset(ModelViewSet):
    """ Отдает элементы выбранного справочника по имени и версии."""
    queryset = UnitManual.objects.all()
    serializer_class = UnitManualSerializer

    def get_queryset(self):
        units = UnitManual.objects.all()
        manual_name = self.request.query_params.get('name', '')
        manual_version = self.request.query_params.get('version', '')
        try:
            if manual_name and not manual_version:
                manual = Manual.objects.filter(
                    name=manual_name,
                    date_commencement__lte=current_date.today()
                )
                manual = manual.latest('date_commencement', 'date_expiration')
                units = units.filter(manual=manual)
            else:
                manual = Manual.objects.get(
                    name=manual_name,
                    version=manual_version,
                )
                units = units.filter(manual=manual)
            return units
        except ObjectDoesNotExist:
            return Response(
                {'errors': 'Запрошенные элементы отсутствуют'},
                status=status.HTTP_404_NOT_FOUND,
            )


class UnitManualValidationViewset(ModelViewSet):
    """ Проверка на то, что элемент с указанным кодом и значением
        присутствует в указанной версии справочника."""
    queryset = UnitManual.objects.all()
    serializer_class = UnitManualSerializer

    def retrieve(self, request, *args, **kwargs):
        data_manual = request.data.get('manual', {})
        data_unit_manual = request.data.get('unit_manual', {})
        try:
            if data_manual.get('version') is not None:
                unit = UnitManual.objects.filter(
                    manual__version=data_manual.get('version'),
                    manual__name=data_manual.get('name'),
                )
            else:
                manual = Manual.objects.filter(
                    name=data_manual.get('name'),
                )
                manual = manual.latest('date_commencement', 'pub_date')
                unit = UnitManual.objects.filter(manual=manual)

            data_code_unit = data_unit_manual.get('code_unit')
            unit = unit.get(code_unit=data_code_unit)
            if data_unit_manual.get('value_unit') == unit.value_unit \
                    or data_unit_manual.get('value_unit') is None:
                serializer = self.get_serializer(unit)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response(
                {'errors': 'Запрошенный элемент отсутствует'},
                status=status.HTTP_404_NOT_FOUND,
            )
