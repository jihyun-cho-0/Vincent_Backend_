from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilterView.as_view(), name='filter_view'),
    path('<int:filter_id>/', views.FilterDetailView.as_view(), name='filter_detail_view'),
    # path('<int:filter_id>/comment/', views.CommentView.as_view(), name='CommentView'),
    # path('<int:filter_id>/comment/<int:coment_id>/', views.CommentDetailView.as_view(), name='CommentDetailView'),
    path('<int:filter_id>/like/', views.FilterLikeView.as_view(), name='filter_like_view'),
]