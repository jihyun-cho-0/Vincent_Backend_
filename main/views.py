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
from filter.models import FilterImage
from rest_framework import status


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
        return self.get_paginated_response(slz.data, status=status.HTTP_200_OK)

class ConvertImageView(APIView):

    def post(self, request):
        slz = TempImageSerializer(data=request.data)
        if slz.is_valid():
            slz.save()
            if slz.data['user_filter']:
                # user_filter가 존재 하면 실행
                change_image(1, slz.data['temp_image'], slz.data['user_filter'])
            else:
                # user_filter가 아닌 기존 filter를 사용하면 실행
                stored_filter = FilterImage.objects.get(id=slz.data['filter']).filter_image
                # filter의 id 값으로 전달될 예정이기 때문에 이미지를 가져와줌
                change_image(2, slz.data['temp_image'], stored_filter)
        else:
            return Response(slz.data, status=status.HTTP_400_BAD_REQUEST)

        return Response(slz.data['temp_image'], status=status.HTTP_200_OK)

        # 이미지 - 1
        # 필터 - 사용자가 원하는 필터 (고른다)
        # 필터2 - 저장된 필터를 고른다.