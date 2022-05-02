from django.shortcuts import get_object_or_404
from shopvisit.models import Visit, Worker, Shop
from rest_framework import viewsets
from .serializers import ShopSerializer, VisitSerializer


class WorkerShopsViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    http_method_names = ['get']

    def get_queryset(self):
        worker = get_object_or_404(
            Worker,
            phone_number=self.request.query_params.get('Authorization')
        )
        return worker.shops.all()


class ShopVisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def perform_create(self, serializer):
        shop = get_object_or_404(
            Shop,
            id=self.kwargs.get('shop_id')
        )
        serializer.save(shop=shop)
