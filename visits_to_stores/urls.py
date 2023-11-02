from django.urls import path
from .views import trading_points_by_phone, add_visit

urlpatterns = [
    path('trading_points/<str:phone_number>/', trading_points_by_phone, name='trading_points_by_phone'),
    path('add_visit/', add_visit, name='add_visit'),
]
