from django.db import models


# Create your models here.

class HelloWorld(models.Model): # DB 에 저장이 된다는 느낌. (내부 파라미터는 신경 x)
    text = models.CharField(max_length=255, null=False)


