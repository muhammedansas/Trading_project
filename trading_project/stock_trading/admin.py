from django.contrib import admin
from .models import Stock

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_name', 'stock_code', 'created_at', 'updated_at')
    search_fields = ('stock_name', 'stock_code')
    list_filter = ('created_at', 'updated_at')
