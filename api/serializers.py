from rest_framework import serializers

from .models import Manual, UnitManual


class UnitManualSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitManual
        fields = '__all__'


class ManualSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manual
        fields = '__all__'
