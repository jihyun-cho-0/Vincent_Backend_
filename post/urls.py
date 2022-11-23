from django.urls import path, include
from post import views
urlpatterns = [
    path('', views.ArticlesView.as_view(), name='ArticlesView'),
    path('<int:post_id>/', views.ArticleDetailView.as_view(), name='ArticleDetailView'),
    path('<int:post_id>/comment/', views.CommentView.as_view(), name='CommentView'),
    path('<int:post_id>/comment/<int:coment_id>/', views.CommentDetailView.as_view(), name='CommentDetailView'),
    path('<int:post_id>/like/', views.LikeView.as_view(), name='LikeView'),
]