from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CartRetrieveUpdateDestroyAPIView, CartListApiView

router = DefaultRouter()
router.register('cart-item', CartItemViewSet, basename='cartitem')


urlpatterns = [
    path('cart/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view()),
    path('cart/', CartListApiView.as_view()),
    path('', include(router.urls))
]