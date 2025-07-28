from rest_framework import serializers
from .models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    owner = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ['id',
                  'owner',
                  'title',
                  'descriptions',
                  'image',
                  'price',
                  'category',
                  'subcategory',
                  'stock',
                  'is_available',
                  'created_at',
                  'updated_at' ]
        read_only_fields = ['owner', 'updated_at', 'created_at']