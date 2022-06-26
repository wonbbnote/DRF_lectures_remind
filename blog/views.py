from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from blog.serializers import ArticleSerializer

from .models import Article, Category

from homework.permission import IsAdminOrAfterSevenDaysFromJoined


# Create your views here.
class PostView(APIView):
    permission_classes = [IsAdminOrAfterSevenDaysFromJoined]

    def get(self, request):
        user = request.user
        print(user)
        today = datetime.now()
        articles = Article.objects.filter(
            exposure_start_date__lte = today,
            exposure_end_date__gte = today
        )
        return Response(ArticleSerializer(articles, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        user = request.user
        title = request.data.get("title", "")
        contents = request.data.get("contents", "")

        category_name = request.data.get("category", "")
        category = Category.objects.get(name=category_name)

        if len(title) <= 5:
            return Response({'error': "제목은 5자 이상!"})
        if len(contents) <= 20:
            return Response({'error': "내용은 20자 이상!"})
        if not category:
            return Response({"error": "카테고리 지정!"})


        new_post = Article.objects.create(author=user, title=title, contents=contents, category=category)
        return Response({"message":"글작성 완료!"}, status = status.HTTP_200_OK)






        
