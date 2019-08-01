# 创建两个表单：一个是更新用户资料时使用，一个是重写用户登录表单。

from django import forms
from .models import User
from django.forms import widgets as wid


class UserInfoForm(forms.ModelForm):
    class Meta:
        # 关联的数据库模型，这里是用户模型
        model = User
        # 验证后可以修改的数据
        fields = ['nickname', 'gender', 'birthday', 'email', 'content']
        # 自定义属性
        widgets = {
            "nickname": wid.TextInput(attrs={"class": "form-control" }),
            "gender": wid.RadioSelect(attrs={},choices=((0, '男'), (1, '女'))),
            'birthday': wid.DateInput(attrs={"class":'form-control form_date'}),
            'email': wid.EmailInput(attrs={"class":"form-control"}),
            'content': wid.Textarea(attrs={"class":"form-control"}),

        }
        labels = {
            "nickname": "用户名",
            'gender'  : '性别',
            #'avatar'  : '头像',
            'birthday': '生日',
            'email'   : '邮箱',
            'content' : "个人简介",
        }
