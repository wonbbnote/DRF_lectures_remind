from rest_framework import serializers
from .models import Product, Review
from user.serializers import UserSerializer
from datetime import datetime
from django.db.models import Avg


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.fullname
        

    class Meta:
        model = Review
        fields = ["user", "content", "created", "rating"]



class ProductSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField()

    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "last_review": ReviewSerializer(reviews.last()).data,
            "average_rating": reviews.aggregate(avg = Avg("rating"))["avg"]
        }


    # writer = UserSerializer()
    writer = serializers.SlugRelatedField(
        read_only = True,
        slug_field="username"
    )
    class Meta:
        model = Product
        fields = ["writer", "title", "thumbnail", "description", "exposure_start_date", "exposure_end_date","review"]
    
    def validate(self, data):
        exposure_end_date = data.get("exposure_end_date", "")
        if exposure_end_date and exposure_end_date < datetime.now().date():
            raise serializers.ValidationError(
                detail = {"error": "유효하지 않은 노출종료 날짜입니다"}
            )
        return data

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        product.description += f"\n\n{product.created_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
        product.save()
        
        return product

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "description":
                # created= getattr(instance, key).split("\n")[-1]
                value += f"\n\n{instance.created_date.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
            setattr(instance, key, value)
        instance.save()
        instance.description = f"{instance.modified_date.replace(microsecond=0, tzinfo =None)}에 수정되었습니다. \n\n"\
            + instance.description 
        instance.save()
        return instance



