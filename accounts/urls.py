from .views import SendOTPView, VerifyOTPView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserInfoViewSet, AddressViewSet

router = DefaultRouter()
router.register('profile', UserInfoViewSet, basename='userinfo')
router.register('address', AddressViewSet, basename='address')


urlpatterns = [
    path('', include(router.urls)),
    path('send-otp/', SendOTPView.as_view()),
    path('verify-otp/', VerifyOTPView.as_view()),
]
