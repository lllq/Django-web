# _*_ encoding:utf8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(choices=(("male", "男"), ("female", "女")), default="male", max_length=6)
    address = models.CharField(max_length=100, default="", verbose_name=u"地址")
    mobile = models.CharField(max_length=11, verbose_name=u"手机号码", null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", verbose_name=u"头像", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecode(models.Model):
    code = models.CharField(verbose_name=u"验证码", max_length=20 )
    email = models.EmailField(verbose_name=u"邮箱", max_length=100)
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码"), ("update_email", u"修改邮箱")), verbose_name=u"验证码", max_length=20)
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name







