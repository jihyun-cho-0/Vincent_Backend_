from django.urls import path
from . import views

urlpatterns = [
    path('', views.FilterView.as_view(), name='filter_view'),
    path('<int:filter_id>/', views.FilterDetailView.as_view(), name='filter_detail_view'),
    path('<int:filter_id>/comment/', views.FilterCommentView.as_view(), name='filter_comment_view'),
    path('<int:filter_id>/comment/<int:coment_id>/', views.FilterCommentDetailView.as_view(), name='filter_comment_detail_view'),
    path('<int:filter_id>/like/', views.FilterLikeView.as_view(), name='filter_like_view'),
]