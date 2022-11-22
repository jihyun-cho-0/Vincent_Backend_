from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from main.paginations import Cursor_created, Cursor_reverse_created, Cursor_likes, Page_created
from post.serializer import PostListSerializer, PostSerializer
from post.models import Post, Comment

# Create your views here.
class MainView(ListAPIView):
    pagination_class = Cursor_created
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
    
    def post(self, reqeust):
        return

class ConvertImageView(APIView):
    def get(self, request):
        return
    
    def post(self, request):
        return