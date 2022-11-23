from django.db import models
from users.models import User


class FilterImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='filter_user')
    filter_name = models.CharField(max_length=25)
    filter_image = models.ImageField(blank=False, upload_to='filter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="filter_likes", blank=True)
    content = models.TextField()

    def __str__(self):
        return str(self.filter_name)

class FilterComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="filter_comment_user")
    filter = models.ForeignKey(FilterImage, on_delete=models.CASCADE, related_name="comment_filter")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="filter_comment_likes", blank=True)
    
    def __str__(self):
        return str(self.comment)