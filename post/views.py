from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from post.serializer import PostCreateSerializer, CommentSerializer, CommentCreateSerializer, PostListSerializer
from post.models import Post
from rest_framework.generics import get_object_or_404
from main.models import TempImage

class ArticlesView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print("####################",request.data)
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class ArticleDetailView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostListSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            serializer = PostListSerializer(post)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("권한이 없습니다.")

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user == post.user:
            post.delete()
            return Response("삭제되었습니다!")
        else:
            return Response("권한이 없습니다.")

class CommentView (APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comment_post.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post_id=post_id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CommentDetailView (APIView):
    def put(self, request, post_id, coment_id):
        comment = get_object_or_404(Post, id=coment_id)
        if request.user == comment.user:
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response("권한이 없습니다.")

    def delete(self, request, post_id, coment_id):
        comment = get_object_or_404(Post, id=coment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("삭제되었습니다!")
        else:
            return Response("권한이 없습니다.")
    
class LikeView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response("unlike", status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            return Response("like", status=status.HTTP_200_OK)