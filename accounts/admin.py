from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserInfo, Address, MessageLog


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('phone', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('phone',)
    ordering = ('-id',)

    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    filter_horizontal = ('groups', 'user_permissions')


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'birth_date')
    search_fields = ('first_name', 'last_name', 'user__phone')
    list_filter = ('gender',)
    readonly_fields = ('avatar',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'get_phone')
    search_fields = ('user__phone', 'address', 'get_phone')
    list_filter = ('user',)


@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'is_verified', 'expires_at', 'created_at', 'is_expired_status')
    search_fields = ('phone', 'code')
    list_filter = ('is_verified', 'created_at')

    def is_expired_status(self, obj):
        return obj.is_expired()
    is_expired_status.short_description = 'Expired?'
    is_expired_status.boolean = True
