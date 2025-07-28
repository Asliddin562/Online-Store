from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Yangi item qo‘shishga imkon beruvchi bo‘sh qator soni

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_type', 'status', 'created_at')
    list_filter = ('delivery_type', 'status', 'created_at')
    search_fields = ('user__phone', 'id')
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    search_fields = ('order__id', 'product__title')
    list_filter = ('product',)
