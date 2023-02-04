from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """用于添加主题的表单"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """添加新条目的表单"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 将文件区域的宽度设置为80 列，默认为40 列
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
