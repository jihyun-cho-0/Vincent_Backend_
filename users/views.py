from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from users import serializers
from users.models import User

from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)
from users.serializers import CustomTokenObtainPairSerializer, UserSerializer, UserProfileSerializer, UserProfileEditSerializer

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user.is_admin = True
        user.save()
        return Response("get 요청")

class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("좋아요 했습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("좋아요 취소 했습니다.", status=status.HTTP_200_OK)



class ProfileView(APIView):  # 프로필 화면 뷰
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class ProfileEditView(APIView): # 프로필 화면 편집 뷰
    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        if request.user == user:
            serializer = UserProfileEditSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("권한이 없습니다.")
