from django.shortcuts import get_object_or_404
from shopvisit.models import Shop, Visit, Worker
from rest_framework import serializers


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
        shop = get_object_or_404(
            Shop,
            id=self.context['view'].kwargs.get('shop_id')
        )
        worker = get_object_or_404(
            Worker,
            phone_number=request.query_params.get('Authorization')
        )
        if shop.worker != worker:
            raise serializers.ValidationError(
                'Указанный номер не привязан к магазину'
            )
        return data

    def create(self, validated_data):
        return Visit.objects.create(**validated_data)

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return VisitGetSerializer(instance, context=context).data
