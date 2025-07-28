from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions
from .models import UserInfo, Address
from .serializers import UserInfoSerializer, AddressSerializer
from .serializers import SendOTPSerializer, VerifyOTPSerializer


class SendOTPView(APIView):
    @extend_schema(
        request=SendOTPSerializer,
        responses={201: None, 400: str},
        description="Telefon raqamni yuboring, tizim sizga OTP yuboradi"
    )
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Kod yuborildi"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    @extend_schema(
        request=VerifyOTPSerializer,
        responses={200: VerifyOTPSerializer, 400: str},
        description="OTP kodni tasdiqlash va JWT olish"
    )
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.validated_data
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return UserInfo.objects.all()
        return UserInfo.objects.filter(user=self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Address.objects.all()
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)