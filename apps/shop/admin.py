from django.contrib import admin

from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'address',
        'phone',
        'rating',
        'is_active',
        'created_at',
    )
    list_filter = ('is_active',)
    search_fields = ('title', 'address', 'phone')