from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from blog.serializers import ArticleSerializer

from .models import Article


# Create your views here.
class PostView(APIView):
    def get(self, request):
        user = request.user
        print(user)
        articles = Article.objects.filter(author=user)
        return Response(ArticleSerializer(articles, many=True).data, status=status.HTTP_200_OK)



        
