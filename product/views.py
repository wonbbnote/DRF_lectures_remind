from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product

from datetime import datetime
from django.db.models import Q

from homework.permission import RegisteredMoreThanThreeDaysUser

# Create your views here.
class ProductView(APIView):
    permission_classes = [RegisteredMoreThanThreeDaysUser]
    def get(self, request):
        today = datetime.now()
        products = Product.objects.filter(
            Q(exposure_start_date__lte = today, exposure_end_date__gte=today)|
            Q(writer= request.user)
        )
        product_serializer = ProductSerializer(products, many=True).data
        return Response(product_serializer, status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        request.data['writer'] = user.id
        product_serializer = ProductSerializer(data =request.data)
        print(request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(product, data =request.data, partial = True)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


