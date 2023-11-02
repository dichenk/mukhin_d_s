# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Worker, TradingPoint, Visit
from .serializers import TradingPointSerializer, VisitSerializer


@api_view(['GET'])
def trading_points_by_phone(request, phone_number):
    try:
        worker = Worker.objects.get(phone_number=phone_number)
    except Worker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    trading_points = TradingPoint.objects.filter(worker=worker)
    serializer = TradingPointSerializer(trading_points, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_visit(request):
    trading_point_id = request.data.get('trading_point_id')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    phone_number = request.data.get('phone_number')

    if not phone_number:
        return Response({"error": "Телефонный номер не предоставлен"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        worker = Worker.objects.get(phone_number=phone_number)
    except Worker.DoesNotExist:
        return Response({"error": "Работник не найден"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        trading_point = TradingPoint.objects.get(id=trading_point_id, worker=worker)
    except TradingPoint.DoesNotExist:
        return Response({"error": "Торговая точка не найдена или не привязана к данному Работнику"}, status=status.HTTP_404_NOT_FOUND)

    visit = Visit.objects.create(trading_point=trading_point, latitude=latitude, longitude=longitude)

    serializer = VisitSerializer(visit)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

