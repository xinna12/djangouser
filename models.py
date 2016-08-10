#coding=utf-8
from django.db import models
from djangouser.profile import UserProfile


class MyProfile(UserProfile):
    real_name = models.CharField(max_length=255)  # 真实姓名
    level = models.IntegerField(default=0)  # 级别
    type = models.IntegerField(default=0) # 类型

class SecondProfile(UserProfile):
    second = models.IntegerField(default=0)