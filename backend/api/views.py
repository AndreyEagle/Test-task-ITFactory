from django.shortcuts import get_object_or_404
from shopvisit.models import Visit, Worker, Shop
from rest_framework import viewsets
from .serializers import ShopSerializer, VisitSerializer
from rest_framework.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

UNAUTHORIZED = 'Авторизуйтесь используя номер телефона'
INVALID_PHONE_NUMBER = 'Неккоректный номер'
NUMBER_NOT_FOUND = 'Указанный номер работника не найден'


class WorkerShopsViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    http_method_names = ['get']

    def get_queryset(self):
        phone_number = self.request.query_params.get('Authorization')
        if phone_number is None:
            logger.error(UNAUTHORIZED)
            raise ValidationError(UNAUTHORIZED)
        if not phone_number.isdigit():
            logger.error(INVALID_PHONE_NUMBER)
            raise ValidationError(INVALID_PHONE_NUMBER)
        worker = Worker.objects.filter(phone_number=phone_number)
        if not worker.exists():
            logger.error(NUMBER_NOT_FOUND)
            raise ValidationError(NUMBER_NOT_FOUND)
        return worker.first().shops.all()


class ShopVisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def perform_create(self, serializer):
        shop = get_object_or_404(
            Shop,
            id=self.kwargs.get('shop_id')
        )
        serializer.save(shop=shop)
