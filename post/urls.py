from django.urls import path
from post import views
urlpatterns = [
    path('', views.PostView.as_view(), name='PostView'),
    path('<int:post_id>/', views.PostDetailView.as_view(), name='PostDetailView'),
    path('<int:post_id>/comment/', views.CommentView.as_view(), name='CommentView'),
    path('<int:post_id>/comment/<int:coment_id>/', views.CommentDetailView.as_view(), name='CommentDetailView'),
    path('<int:post_id>/like/', views.LikeView.as_view(), name='LikeView'),
]