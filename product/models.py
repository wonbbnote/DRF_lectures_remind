from django.db import models

# Create your models here.
class Product(models.Model):
    writer = models.ForeignKey("user.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    thumbnail = models.FileField("썸네일", upload_to="product/image")
    description = models.TextField("설명")
    created_date = models.DateTimeField("등록시간", auto_now_add=True)
    modified_date = models.DateTimeField("수정시간", auto_now=True)
    exposure_start_date = models.DateField("노출 시작일")
    exposure_end_date = models.DateField("노출 종료일자")
    is_active = models.BooleanField("활성화여부", null=True)
    price = models.IntegerField("가격", null=True)


class Review(models.Model):
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    content= models.TextField("내용")
    created = models.DateField("등록시간", auto_now_add=True)
    rating = models.IntegerField("평점")
    
