from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product
User = get_user_model()


class Order(models.Model):
    class DeliveryType(models.TextChoices):
        DELIVERY = 'Delivery', 'delivery'
        PICKUP = 'Pickup', 'pickup'

    class Status(models.TextChoices):
        CREATED = 'Created', 'created'
        PROCESSING = 'Processing', 'processing'
        COMPLETED = 'Completed', 'completed'
        CANCELED = 'Canceled', 'canceled'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(max_length=10, choices=DeliveryType.choices)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.CREATED)

    def __str__(self):
        return f"Order #{self.id} - {self.user.phone}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} x {self.quantity}"
