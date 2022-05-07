from django.contrib import admin
from .models import Worker, Shop, Visit


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone_number',
    )
    search_field = ('name')
    empty_value_display = '-пусто-'


class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'worker',
    )
    search_field = ('name')
    empty_value_display = '-пусто-'


class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'shop',
        'latitude',
        'longtitude',
    )
    search_fields = (
        'shop__name',
        'shop__worker__name'
    )
    empty_value_display = '-пусто-'


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Visit, VisitAdmin)
