from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from filter.serializer import FilternameSerializer, FilterallSerializer, FilterCommentSerializer, CommentCreateSerializer
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

class FilterDetailView(APIView):
    def get(self, request):
        return

class FilterLikeView(APIView):
    def get(self, request):
        return
# class FilterView(APIView):
#     def get(self, request):
#         post = Post.objects.all()
#         serializer = PostListSerializer(post, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = PostCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class ArticleDetailView(APIView):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         serializer = PostListSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         if request.user == post.user:
#             serializer = PostListSerializer(post)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         else:
#             return Response("권한이 없습니다.")

#     def delete(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         if request.user == post.user:
#             post.delete()
#             return Response("삭제되었습니다!")
#         else:
#             return Response("권한이 없습니다.")

# class CommentView (APIView):
#     def get(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         comments = post.comment_post.all()
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)

#     def post(self, request, post_id):
#         serializer = CommentCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user, post_id=post_id)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class CommentDetailView (APIView):
#     def put(self, request, post_id, coment_id):
#         comment = get_object_or_404(Post, id=coment_id)
#         if request.user == comment.user:
#             serializer = CommentCreateSerializer(comment, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         else:
#             return Response("권한이 없습니다.")

#     def delete(self, request, post_id, coment_id):
#         comment = get_object_or_404(Post, id=coment_id)
#         if request.user == comment.user:
#             comment.delete()
#             return Response("삭제되었습니다!")
#         else:
#             return Response("권한이 없습니다.")
    
# class LikeView(APIView):
#     def post(self, request, post_id):
#         post = get_object_or_404(Post, id=post_id)
#         if request.user in post.likes.all():
#             post.likes.remove(request.user)
#             return Response("unlike", status=status.HTTP_200_OK)
#         else:
#             post.likes.add(request.user)
#             return Response("like", status=status.HTTP_200_OK)