from django.db import models
from django.contrib.auth import get_user_model
import uuid
import os

User = get_user_model()

def product_image_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('products/', filename)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="subcategories")

    def __str__(self):
        return self.name


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255, blank=True)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(upload_to=product_image_upload_path, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,  related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

