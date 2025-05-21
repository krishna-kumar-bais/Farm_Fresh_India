from django.contrib import admin
from .models import Category, Product, Farmer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'sub_category', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category_type', 'sub_category']
    search_fields = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location', 'description']
    filter_horizontal = ['products']
