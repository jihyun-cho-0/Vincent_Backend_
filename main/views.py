from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from main.paginations import Cursor_created, Cursor_reverse_created, Cursor_likes, Page_created
from post.serializer import PostListSerializer, PostSerializer
from post.models import Post, Comment
from main.deeprun import change_image
from main.serializer import TempImageSerializer
from main.models import TempImage
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.
class MainView(ListAPIView):
    pagination_class = Cursor_created
    # pagination_class = Page_created
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

    def get(self, request):
        sorting_val = self.request.GET.get('sort')
        # get 파라미터 내용중 sort 문자열의 내용을 가져옴
        if sorting_val == 'recreate':
            self.pagination_class = Cursor_reverse_created
        if sorting_val == 'like':
            self.pagination_class = Cursor_likes
        pages = self.paginate_queryset(self.get_queryset())
        # pages 라는 변수에 get_queryset을 이용하여 queryset을 가져오고 pagination에 넣어줌
        slz = self.get_serializer(pages, many=True)
        return self.get_paginated_response(slz.data)

class ConvertImageView(APIView):
    def get(self, request):

        return Response('test')
    
    def post(self, request):
        slz = TempImageSerializer(data=request.data)
        # {'id': 7, 'temp_image': '/media/temp/11_fg7op5y.png', 'user_filter': '/media/user_temp_filter/testgo1_2MT8aiv.jpg', 'filter': None}
        if slz.is_valid():
            slz.save()
            if slz.data['user_filter']:
                change_image(slz.data['temp_image'], slz.data['user_filter'])


        return Response('test')