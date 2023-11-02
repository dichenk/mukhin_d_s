from django.contrib import admin
from .models import Worker, TradingPoint, Visit


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']
    search_fields = ['name']


class TradingPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'worker']
    search_fields = ['name']


class VisitAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'trading_point', 'latitude', 'longitude']
    search_fields = ['trading_point__name', 'trading_point__worker__name']


admin.site.register(Worker, WorkerAdmin)
admin.site.register(TradingPoint, TradingPointAdmin)
admin.site.register(Visit, VisitAdmin)
