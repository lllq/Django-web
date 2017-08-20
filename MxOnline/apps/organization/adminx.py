# _*_ coding:utf-8 _*_
# __author__ = 'll'

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_play = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc']

xadmin.site.register(CityDict, CityDictAdmin)


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'students', 'image', 'address', 'add_time', 'course_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'students', 'address', 'course_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'students', 'address', 'add_time', 'course_nums']
    relfield_style = 'fk-ajax'

xadmin.site.register(CourseOrg, CourseOrgAdmin)


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(Teacher, TeacherAdmin)



