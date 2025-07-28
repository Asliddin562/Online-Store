from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemSerializer, CartListSerializer, CartRetrieveUpdateDestroySerializer
from .models import Cart, CartItem
from rest_framework import generics


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartRetrieveUpdateDestroySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cart.objects.prefetch_related('items__product')
        return Cart.objects.filter(user=user).prefetch_related('items__product')


class CartListApiView(generics.ListAPIView):
    serializer_class = CartListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cart.objects.prefetch_related('items__product')
        return Cart.objects.filter(user=user).prefetch_related('items__product')



class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Cart.objects.prefetch_related('items__product')
        return Cart.objects.filter(user=user).prefetch_related('items__product')


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CartItem.objects.all()
        return CartItem.objects.filter(cart__user=self.request.user)

