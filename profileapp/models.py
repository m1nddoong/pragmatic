from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # Profile 과 user 를 하나씩 연결해준다.
    # 사용자 한명당 프로필 몇 개를, 혹은 게시글 몇 개를 연결시킬 것인지를 나타내는 것이 OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # temp_profile 객체 생성
        return super().form_valid(form)