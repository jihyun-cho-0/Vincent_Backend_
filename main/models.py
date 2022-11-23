from django.db import models
from filter.models import FilterImage

class TempImage(models.Model):
    temp_image = models.ImageField(blank=False, upload_to='temp')
    # 원본 이미지
    filter = models.ForeignKey(FilterImage, blank=True, null=True, on_delete=models.CASCADE, related_name='temp_filter')
    # 서버에 저장된 filter_image의 id
    user_filter = models.ImageField(blank=False, null=True, upload_to='user_temp_filter')
    # 사용자가 같이 보낸 filter