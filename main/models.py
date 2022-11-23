from django.db import models
from filter.models import FilterImage

class TempImage(models.Model):
    temp_image = models.ImageField(blank=False, upload_to='temp')
    filter = models.ForeignKey(FilterImage, blank=True, null=True, on_delete=models.CASCADE, related_name='temp_filter')
    user_filter = models.ImageField(blank=False, null=True, upload_to='user_temp_filter')