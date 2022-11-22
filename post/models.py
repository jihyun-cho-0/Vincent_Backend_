from django.db import models
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_image = models.ImageField(blank=True, upload_to='post/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)
    
    def __str__(self):
        return str(self.comment)