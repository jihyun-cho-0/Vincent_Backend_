from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from filter.serializer import FilternameSerializer, FilterallSerializer, FilterCommentSerializer, CommentCreateSerializer, FiltercreateSerializer
from filter.models import FilterComment, FilterImage
from main.paginations import Cursor_created, Cursor_reverse_created, Cursor_likes, Page_created
from rest_framework.generics import ListAPIView

class FilterView(ListAPIView):
    pagination_class = Cursor_created
    serializer_class = FilterallSerializer
    queryset = FilterImage.objects.all()

    def get(self, request):
        sorting_val = self.request.GET.get('sort')
        # get 파라미터 내용중 sort 문자열의 내용을 가져옴
        if sorting_val == 'recreate':
            # 최신 순 정렬
            self.pagination_class = Cursor_reverse_created
        if sorting_val == 'like':
            # 좋아요 순 정렬
            self.pagination_class = Cursor_likes
        pages = self.paginate_queryset(self.get_queryset())
        # pages 라는 변수에 get_queryset을 이용하여 queryset을 가져오고 pagination에 넣어줌
        slz = self.get_serializer(pages, many=True)
        return self.get_paginated_response(slz.data)
    
    def post(self, request, format=None):
        slz = FiltercreateSerializer(data=request.data)
        if slz.is_valid():
            slz.save(user=request.user)
            return Response(slz.data)
        else:
            return Response(slz.errors)

class FilterDetailView(APIView):
    def get(self, request, filter_id):
        filter_post = get_object_or_404(FilterImage, id=filter_id)
        slz = FilterallSerializer(filter_post)
        return Response(slz.data, status=status.HTTP_200_OK)
    
    def put(self, request, filter_id):
        filter_post = get_object_or_404(FilterImage, id=filter_id)
        if request.user == filter_post.user:
            slz = FilterallSerializer(filter_post)
            if slz.is_valid():
                slz.save()
                return Response(slz.data)
            else:
                return Response(slz.errors)
        else:
            return Response("권한이 없습니다.")
    
    def delete(self, request, filter_id):
        filter_post = get_object_or_404(FilterImage, id=filter_id)
        if request.user == filter_post.user:
            filter_post.delete()
            return Response("삭제되었습니다!")
        else:
            return Response("권한이 없습니다.")

class FilterLikeView(APIView):
    def post(self, request, filter_id):
        filter_post = get_object_or_404(FilterImage, id=filter_id)
        if request.user in FilterImage.likes.all():
            filter_post.likes.remove(request.user)
            return Response("unlike", status=status.HTTP_200_OK)
        else:
            filter_post.likes.add(request.user)
            return Response("like", status=status.HTTP_200_OK)

class FilterCommentView (APIView):
    def get(self, request, filter_id):
        filter_post = get_object_or_404(FilterImage, id=filter_id)
        comments = filter_post.filter_comment_likes.all()
        slz = FilterCommentSerializer(comments, many=True)
        return Response(slz.data)

    def post(self, request, filter_id):
        slz = CommentCreateSerializer(data=request.data)
        if slz.is_valid():
            slz.save(user=request.user, filter_id=filter_id)
            return Response(slz.data)
        else:
            return Response(slz.errors)

class FilterCommentDetailView (APIView):
    def put(self, request, filter_id, coment_id):
        comment = get_object_or_404(FilterImage, id=coment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("권한이 없습니다.")

    def delete(self, request, filter_id, coment_id):
        comment = get_object_or_404(FilterImage, id=coment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("삭제되었습니다!")
        else:
            return Response("권한이 없습니다.")