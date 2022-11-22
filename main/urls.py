from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main_view'),
    path('image/', views.ConvertImageView.as_view(), name='convert_image_view'),
]