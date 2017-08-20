# _*_ coding:utf-8 _*_
# __author__ = 'll'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from django.contrib.auth.models import User
from .models import EmailVerifyRecode, Banner, UserProfile


class UserProfileAdmin(UserAdmin):
    pass

# xadmin.site.register(UserProfile, UserProfileAdmin)


class BaseSetting(object):
    enable_themes = True
    user_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSettings)


class EmailverifyRecodeAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'eamil', 'send_type']
    model_icon = 'fa fa-handshake-o'

xadmin.site.register(EmailVerifyRecode, EmailverifyRecodeAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'url', 'index', 'add_time']
    search_fields = ['title', 'url', 'index']


xadmin.site.register(Banner, BannerAdmin)
# xadmin.site.unregister(User)