"""定义learning_logs 的URL 模式"""
from django.urls import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),

    # 显示所有的主题
    path('topics/', views.topics, name='topics'),

    # 显示特定主题的详细页面
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # 用于添加新主题的网页
    path('new_topic', views.new_topic, name='new_topic'),
]
