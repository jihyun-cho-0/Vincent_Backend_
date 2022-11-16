from django.db import models
from users.models import User


class FilterImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filter_user')
    filter_name = models.CharField(max_length=25)
    filter_image = models.ImageField(blank=False, upload_to='filter/%Y/%m/')

    def __str__(self):
        return str(self.filter_name)