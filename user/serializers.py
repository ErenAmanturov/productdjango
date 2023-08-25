from rest_framework import serializers
from user.models import User
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})
        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True

        super().__init__(*args, **kwargs)


class RegisterSerializer(serializers.ModelSerializer):
    """Модельный Сериализатор Регистрации Пользователя"""
    username = serializers.CharField(max_length=10, required=True)
    phone = PhoneNumberField(required=True)
    password = PasswordField(required=True, allow_blank=False, allow_null=False)

    class Meta:
        model = User
        fields = ["email", "username", 'phone', "password"]

    def validate(self, attrs):
        if 4 < len(attrs['password']) < 10:
            return attrs
        raise serializers.ValidationError({
            'message': _("Must be more than 4 characters and less than 10")
        })

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    # password = PasswordField(required=True, allow_null=False, allow_blank=False)
    password = serializers.CharField()


class ChangePasswordSerializers(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class Pass:
    pass