from django.db import models
from django.utils import timezone


class Worker(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TradingPoint(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, related_name='trading_points', null=True)

    def __str__(self):
        return self.name


class Visit(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    trading_point = models.ForeignKey(TradingPoint, on_delete=models.SET_NULL, related_name='visits', null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "Посещение {} в {}".format(self.timestamp, self.trading_point.name if self.trading_point else 'Неизвестная точка')
    
