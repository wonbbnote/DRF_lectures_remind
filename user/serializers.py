from rest_framework import serializers
from .models import User, UserProfile
from blog.serializers import ArticleSerializer, CommentSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    user_articles = ArticleSerializer(many=True, source="article_set")
    user_comments = CommentSerializer(many=True, source ="comment_set")
    
    
    class Meta:
        model = User
        fields = ["username", "userprofile", "user_comments", "user_articles"]