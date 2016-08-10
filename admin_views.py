#coding=utf-8

import pdb

from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


def user_view(request):
    return render_to_response(
        "user.html",
        {'book_list' : User.objects.all()},
        RequestContext(request, {}),
    )
user_view = staff_member_required(user_view)