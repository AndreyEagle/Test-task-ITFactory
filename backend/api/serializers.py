from django.shortcuts import get_object_or_404
from shopvisit.models import Shop, Visit, Worker
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)

UNAUTHORIZED = 'Авторизуйтесь используя номер телефона'
INVALID_PHONE_NUMBER = 'Неккоректный номер'
WORKER_NUMBER_NOT_FOUND = 'Указанный номер работника не найден'
PHONE_NUMBER_NO_SHOP = 'Указанный номер не привязан к магазину'


class ShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
        )
        model = Shop


class VisitGetSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = (
            'id',
            'date'
        )
        model = Visit


class VisitSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    shop = serializers.PrimaryKeyRelatedField(read_only=True)
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        fields = (
            'id',
            'shop',
            'latitude',
            'longtitude',
            'date'
        )
        model = Visit

    def validate(self, data):
        request = self.context.get('request')
        phone_number = request.query_params.get('Authorization')
        if phone_number is None:
            logger.error(UNAUTHORIZED)
            raise serializers.ValidationError(UNAUTHORIZED)
        if not phone_number.isdigit():
            logger.error(INVALID_PHONE_NUMBER)
            raise serializers.ValidationError(INVALID_PHONE_NUMBER)
        shop = get_object_or_404(
            Shop,
            id=self.context['view'].kwargs.get('shop_id')
        )
        worker = Worker.objects.filter(phone_number=phone_number)
        if not worker.exists():
            logger.error(WORKER_NUMBER_NOT_FOUND)
            raise serializers.ValidationError(WORKER_NUMBER_NOT_FOUND)
        if shop.worker != worker.first():
            logger.error(PHONE_NUMBER_NO_SHOP)
            raise serializers.ValidationError(PHONE_NUMBER_NO_SHOP)
        return data

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return VisitGetSerializer(instance, context=context).data
