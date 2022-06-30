from rest_framework import serializers
from reviews.models import User
# TODO импортировать размер полей из сетинг

class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254, required=True)
    username = serializers.CharField(max_length=150, required=True)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError('Нельзя использовать логин me')
        return data

    class Meta:
        fields = ('username', 'email')


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=True)
    confirmation_code = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )






















"""

from django.contrib.auth.validators import ASCIIUsernameValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from api_yamdb.settings import CODE_LENGTH, EMAIL_LENGTH, USERNAME_LENGTH
from reviews import models


class UsernameSerializer(serializers.Serializer):
    
    def not_me_username_validation(value):
        if value == 'me':
            raise ValidationError(
                'Нельзя использовать "me" в качестве имени пользователя.')
    
    
    username = serializers.CharField(
        max_length=USERNAME_LENGTH,
        validators=[ASCIIUsernameValidator(),
                    not_me_username_validation])


class UsernameCodeSerializer(UsernameSerializer):
    confirmation_code = serializers.CharField(
        max_length=CODE_LENGTH)


class SignUpSerializer(UsernameSerializer):
    email = serializers.EmailField(
        max_length=EMAIL_LENGTH)


class UserSerializer(serializers.ModelSerializer,
                     UsernameSerializer):

    def validate_username(self, value):
        if models.User.objects.filter(username=value).exists():
            raise ValidationError(
                f'Имя пользователя {value} уже существует.')
        return value

    class Meta:
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )
        model = models.User


class MeSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        read_only_fields = ('role',)



"""
