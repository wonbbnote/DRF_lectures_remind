from rest_framework import serializers

from .models import Article, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = ["author", "title", "category", "contents"]