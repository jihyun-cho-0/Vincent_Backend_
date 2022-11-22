from rest_framework import serializers
from filter.models import FilterImage, FilterComment

class FilternameSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilterImage
        fields = ("filter_name",)

class FiltercreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterImage
        fields = "__all__"

class FilterallSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_likes_count(self, obj):
        return obj.likes.count()
    
    def get_comments_count(self, obj):
        return obj.comment_filter.count()
    
    class Meta:
        model = FilterImage
        fields = ("pk", "user", "filter_name", "filter_image", "likes_count", "comments_count", "likes_count",)

class FilterCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = FilterComment
        exclude = ("filter", )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterComment
        fields = ("content",)