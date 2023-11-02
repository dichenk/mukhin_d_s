from rest_framework import serializers
from .models import TradingPoint, Visit


class TradingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingPoint
        fields = ['id', 'name']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'timestamp']
