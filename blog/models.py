from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=30)
    description = models.TextField("설명")

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contents = models.TextField("글 내용")
    exposure_start_date = models.DateField("노출 시작 일자", null=True)
    exposure_end_date = models.DateField("노출 종료 일자", null=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey("user.USER", on_delete=models.CASCADE)
    contents = models.TextField("내용")


