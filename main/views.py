from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from main.paginations import Cursor_created, Cursor_reverse_created
from post.serializer import PostListSerializer, PostSerializer
from post.models import Post, Comment

# Create your views here.
class MainView(ListAPIView):
    pagination_class = Cursor_created
    serializer_class = PostListSerializer
    queryset = Post.objects.all()

    def get(self, request):
        if self.request.Get.get(''):
            pass
        return
    
    def post(self, reqeust):
        return

class ConvertImageView(APIView):
    def get(self, request):
        return
    
    def post(self, request):
        return