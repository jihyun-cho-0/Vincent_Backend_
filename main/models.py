from django.db import models
from filter.models import FilterImage
import os
from django.conf import settings


class TempImage(models.Model):
    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(TempImage, self).delete(*args, **kargs)
    
    temp_image = models.ImageField(blank=False, upload_to='temp')
    # 원본 이미지
    filter = models.ForeignKey(FilterImage, blank=True, null=True, on_delete=models.CASCADE, related_name='temp_filter')
    # 서버에 저장된 filter_image의 id
    user_filter = models.ImageField(blank=False, null=True, upload_to='user_temp_filter')
    # 사용자가 같이 보낸 filter