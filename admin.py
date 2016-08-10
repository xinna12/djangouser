#coding=utf-8

import pdb

from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from djangouser.models import MyProfile
from djangouser.models import SecondProfile

def get_profile_fields(ProfileClass):
    fields = []
    attrs = dict(ProfileClass.__dict__)
    module = attrs.pop('__module__')
    for obj_name, obj in attrs.items():
        if isinstance(obj, models.Field): fields.append(obj_name)
    return fields

def get_profile_name(ProfileClass):
    profile_name = ProfileClass.__bases__[0].__name__
    return profile_name

UserAdmin.fieldsets = list(UserAdmin.fieldsets)
UserAdmin.fieldsets.append((get_profile_name(MyProfile), {'fields': get_profile_fields(MyProfile) + get_profile_fields(SecondProfile)}))
