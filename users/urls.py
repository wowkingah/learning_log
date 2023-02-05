"""为应用程序 users 定义 URL 模式"""
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # 登录页面，第二个参数为 Django 内置登陆视图，让请求发送给 Django 默认类 as_view
    # 因没编写自己的视图函数，指定用户登录视图所使用的模板
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),

    # 注销
    path('logout/', views.logout_view, name='logout'),
]
