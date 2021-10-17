from rest_framework import serializers

from .models import Manual, UnitManual


class UnitManualSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitManual
        fields = ('id', 'code_unit', 'value_unit', 'pub_date', )


class ManualSerializer(serializers.ModelSerializer):
    manual = UnitManualSerializer(source='units', many=True)

    class Meta:
        model = Manual
        fields = ('id', 'name', 'short_name', 'description',
                  'version', 'commencement_date', 'manual', )


class UnitManualListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitManual
        fields = ('id', 'code_unit', 'value_unit', 'pub_date', 'manual')
