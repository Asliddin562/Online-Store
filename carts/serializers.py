from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source="product.title")

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_title', 'quantity']
        

    def create(self, validated_data):
        request = self.context["request"]
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            cart = Cart.objects.create(user=request.user)
        return CartItem.objects.create(cart=cart, **validated_data)


class CartRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Cart.objects.create(user=user)


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user']
        read_only_fields = ['user', 'created_at']

