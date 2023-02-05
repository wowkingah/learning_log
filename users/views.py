from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout


# Create your views here.
def logout_view(reqeust):
    """注销用户"""
    logout(reqeust)
    return HttpResponseRedirect(reverse('learning_logs:index'))
