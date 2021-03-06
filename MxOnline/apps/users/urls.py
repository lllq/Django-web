# _*_ coding:utf-8 _*_
# __author__ = 'll'

from django.conf.urls import url

from users.views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from users.views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView
from users.views import MyFavCourseView, MyMessageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name="user_info"),
    # 用户头头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),

    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),

    # 修改邮箱验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),

    # 修改邮箱验证码
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 个人中心用户机构收藏
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

    # 个人中心用户讲师收藏
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

    # 个人中心用户课程收藏
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),

    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage")
]
