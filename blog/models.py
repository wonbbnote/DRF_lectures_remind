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




