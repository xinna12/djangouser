#coding=utf-8
import pdb
from django.db import models
from django.utils.importlib import import_module
from django.contrib.auth.models import User

profile_model_map = {
    "UserProfile":User,
}

class ProfileBase(type):  # 对于传统类，他们的元类都是types.ClassType
    def __new__(cls, name, bases, attrs):  # 带参数的构造器，__new__一般用于设置不变数据类型的子类
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            profile_name = parents[0].__name__
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                profile_model_map[profile_name].add_to_class(obj_name, obj)
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)

class UserProfile(object):
    __metaclass__ = ProfileBase  # 类属性