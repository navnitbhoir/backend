# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import update_last_login
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import User

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         user = authenticate(username=data.get('email'), password=data.get('password'))
#         if not user:
#             raise serializers.ValidationError("Invalid email or password")
#         if not user.is_active:
#             raise serializers.ValidationError("User account is disabled")
#         data['user'] = user
#         return user

    # def create(self, validated_data):
    #     user = validated_data
    #     refresh = RefreshToken.for_user(user)
    #     update_last_login(None, user)
    #     return {
    #         'user': user.username,
    #         'role': user.role,
    #         'refresh': str(refresh),
    #         'access': str(refresh.access_token),
    #     }
from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")

        data['user'] = user
        return data
