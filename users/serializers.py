from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
# from posts.serializers import PostListSerializer



class UserProfileSerializer(serializers.ModelSerializer):
    # followers = serializers.StringRelatedField(many=True)
    # followings = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ("username", "email", "profile_image", "is_active", "followings")


class UserProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "profile_image")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

