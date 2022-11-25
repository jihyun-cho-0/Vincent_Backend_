from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='main_view'),
    path('image/', views.ConvertImageView.as_view(), name='convert_image_view'),
    path('<int:temp_id>/', views.Temp_Image_Del_View.as_view(), name='temp_image_del_view'),
]