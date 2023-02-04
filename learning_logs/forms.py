from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    """用于添加主题的表单"""
    class Meta:
        model = Topic
        fields = {'text'}
        labels = {'text': ''}
