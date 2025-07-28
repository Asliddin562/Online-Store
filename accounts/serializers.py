from rest_framework import serializers
from .models import MessageLog
from .utils import generate_otp, to_clean_phone
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import UserInfo, Address

User = get_user_model()



class SendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13, min_length=12)

    def validate_phone(self, value):
        if not value.startswith("+998") and not value.startswith("998"):
            raise serializers.ValidationError("Telefon raqam +998 yoki 998 bilan boshlanish kerak")
        return value

    def create(self, validated_value):
        phone = to_clean_phone(validated_value["phone"])
        code = generate_otp()
        expires_at = timezone.now() + timezone.timedelta(minutes=3)

        print(f"[TEST] Sizga kod yuborildi {code}")
        return MessageLog.objects.create(
            phone=phone,
            code=code,
            expires_at=expires_at)


class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        phone = data.get(to_clean_phone("phone"))
        code = data.get("code")
        try:
            log = MessageLog.objects.filter(phone=phone, code=code, is_verified=False).latest("created_at")
        except MessageLog.DoesNotExist:
            raise serializers.ValidationError("Telefon raqam yoki parol xato")

        if log.is_expired()==True:
            raise serializers.ValidationError("Parolni muddati o'tgan")

        log.is_verified = True
        log.save()

        user, created = User.objects.get_or_create(phone=phone)
        tokens = RefreshToken.for_user(user)
        print(f"[TEST] verify ishladi {code}")
        return {
            'token': str(tokens),
            'access': str(tokens.access_token),
            'created_user': created
        }

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            'id',
            'first_name',
            'last_name',
            'address',
            'avatar',
            'birth_date',
            'gender',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        # Token orqali foydalanuvchini avtomatik biriktirish
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # update-da userni o‘zgartirish kerak emas
        validated_data.pop('user', None)
        return super().update(instance, validated_data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user', 'address', 'yandex_link', 'google_link', 'get_phone']







