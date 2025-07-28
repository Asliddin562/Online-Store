from rest_framework import serializers
from carts.models import Cart
from orders.models import Order, OrderItem
from accounts.models import Address
from products.models import Product


class CheckoutSerializer(serializers.Serializer):
    delivery_type = serializers.ChoiceField(choices=Order.DeliveryType.choices)
    address_id = serializers.IntegerField(required=False)

    def validate(self, attrs):
        delivery_type = attrs.get("delivery_type")
        address_id = attrs.get("address_id")
        user = self.context["request"].user

        if delivery_type == Order.DeliveryType.DELIVERY:
            if not address_id:
                raise serializers.ValidationError({"address_id": "Address ID majburiy."})
            if not Address.objects.filter(id=address_id, user=user).exists():
                raise serializers.ValidationError({"address_id": "Bu manzil bu user uchun mavjud emas."})

        return attrs

    def save(self, **kwargs):
        user = self.context["request"].user
        delivery_type = self.validated_data["delivery_type"]
        address_id = self.validated_data.get("address_id")

        cart = Cart.objects.prefetch_related("items__product").filter(user=user).first()
        if not cart or not cart.items.exists():
            raise serializers.ValidationError("Sizning savatingiz bo'sh.")

        address = None
        if delivery_type == Order.DeliveryType.DELIVERY:
            address = Address.objects.get(id=address_id, user=user)

        order = Order.objects.create(
            user=user,
            delivery_type=delivery_type,
            status=Order.Status.CREATED,
            address=address
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity)

        cart.items.all().delete()
        cart.delete()

        return order


