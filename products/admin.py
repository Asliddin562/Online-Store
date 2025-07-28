from django.contrib import admin
from .models import Category, SubCategory, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['name']
    list_filter = ['category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'price', 'stock', 'is_available', 'created_at']
    list_filter = ['is_available', 'created_at', 'category', 'subcategory']
    search_fields = ['title', 'owner__phone']
    readonly_fields = ['created_at', 'updated_at']
    autocomplete_fields = ['owner', 'category', 'subcategory']
    list_editable = ['price', 'stock', 'is_available']
