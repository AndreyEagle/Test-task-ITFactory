from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import WorkerShopsViewSet, ShopVisitViewSet

app_name = 'shopvisit'
app_name = 'api'

router = DefaultRouter()
router.register(r'shops', WorkerShopsViewSet, basename='shops')
router.register(
    r'shops/(?P<shop_id>\d+)/visit',
    ShopVisitViewSet,
    basename='shopvisit'
)


urlpatterns = [
    path('', include(router.urls)),
]
