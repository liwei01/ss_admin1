# -*- coding: utf-8
from django import forms



#login表单模型
#定义的登录表单有两个域username和password，这两个域都为必填项。
class LoginForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )
    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm,self).clean()

#定义注册表单模型
class RegisterForm(forms.Form):
    username = forms.CharField(
            required = True,
            label=u"用户名",
            error_messages={'required':'请输入用户名'},
            widget=forms.TextInput(
                attrs={
                    'placeholder':u"用户名",
                    }
                )
            )
    password = forms.CharField(
            required=True,
            label=u"密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )
    password1 = forms.CharField(
            required=True,
            label=u"确认密码",
            error_messages={'required':u'请输入密码'},
            widget=forms.PasswordInput(
                attrs={
                    'placeholder':u"密码",
                    }
                ),
            )
    email = forms.CharField(
            required=True,
            label=u"电子邮件",
            error_messages={'required':u'电子邮件'},
            widget=forms.EmailInput(
                attrs={
                    'placeholder':u"电子邮件",
                    }
                ),
            )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"用户名和密码为必填项")
        else:
            password = self.cleaned_data.get("password")
            password1 = self.cleaned_data.get("password1")
            if password != password1 :
                raise forms.ValidationError(u"两次输入的密码不一样")

            else:
                cleaned_data = super(RegisterForm,self).clean()
