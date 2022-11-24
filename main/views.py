from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from main.paginations import post_page, filter_modal_page
from post.serializer import PostListSerializer, PostSerializer
from post.models import Post, Comment
from main.deeprun import change_image
from main.serializer import TempImageSerializer
from main.models import TempImage
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from filter.models import FilterImage
from rest_framework import status
from django.db.models import Count


# Create your views here.
class MainView(ListAPIView):
    pagination_class = post_page
    serializer_class = PostListSerializer
    queryset = Post.objects.all().order_by('-created_at')
    # 초기는 최신순 정렬
    # queryset = Post.objects.annotate(count=Count('likes')).order_by('-count')

    def get(self, request):
        sorting_val = self.request.GET.get('sort')
        # get 파라미터 내용중 sort 문자열의 내용을 가져옴
        if sorting_val == 'recreate':
            self.queryset = Post.objects.all().order_by('created_at')

        if sorting_val == 'like':
            self.queryset = Post.objects.annotate(count=Count('likes')).order_by('-count')
            # 좋아요 순으로 정렬
        
        pages = self.paginate_queryset(self.get_queryset())
        # pages 라는 변수에 get_queryset을 이용하여 queryset을 가져오고 pagination에 넣어줌
        # pagination이 실행될때 필요한 구문, 하지만 안 씀

        slz = self.get_serializer(pages, many=True)
        return self.get_paginated_response(slz.data)

class ConvertImageView(APIView):

    def post(self, request):
        slz = TempImageSerializer(data=request.data)
        if slz.is_valid():
            slz.save()
            if slz.data['user_filter']:
                # user_filter가 존재 하면 실행
                # 방금 저장한 모델 pk 값 가져와서 temp_image 값 가져와서 넣어주기
                change_image(1, slz.data['temp_image'], slz.data['user_filter'])
            elif slz.data['filter']:
                # user_filter가 아닌 기존 filter를 사용하면 실행
                stored_filter = FilterImage.objects.get(id=slz.data['filter']).filter_image
                # filter의 id 값으로 전달될 예정이기 때문에 이미지를 가져와줌
                change_image(2, slz.data['temp_image'], stored_filter)
        else:
            return Response(slz.data, status=status.HTTP_400_BAD_REQUEST)

        return Response(slz.data['temp_image'], status=status.HTTP_200_OK)