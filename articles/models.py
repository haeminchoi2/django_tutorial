from django.db import models

# Create your models here.
class Article(models.Model): # 상속
    # id는 자동으로 만들어 진다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)