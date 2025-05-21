from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'city', 'state', 'payment_method', 'status', 'created']
    list_filter = ['status', 'created', 'payment_method']
    search_fields = ['full_name', 'email', 'phone', 'city', 'state']
    inlines = [OrderItemInline]
    list_editable = ['status']
