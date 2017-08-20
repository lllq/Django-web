# _*_ coding:utf-8 _*_
# __author__ = 'll'
import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg

class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time', 'category','get_zj_nums']
    search_fields = ['name', 'degree', 'students', 'fav_nums', 'click_nums', 'category']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time', 'category']
    model_icon = 'fa fa-user'
    ordering = ["-click_nums"]
    readonly_fields = ['name']
    list_editable = ['name', 'degree', 'learn_times', 'students', 'fav_nums', 'category']
    inlines = [LessonInline, CourseResourceInline]
    style_fields = {"detail": "ueditor"}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner = False)
        return qs

    def save_models(self):
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)

xadmin.site.register(Course, CourseAdmin)


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time', 'category']
    search_fields = ['name', 'degree', 'students', 'fav_nums', 'click_nums', 'category']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time', 'category']
    model_icon = 'fa fa-user'
    style_fields = {"detail": "ueditor"}
    ordering = ["-click_nums"]
    readonly_fields = ['name']
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner = True)
        return qs

xadmin.site.register(BannerCourse, BannerCourseAdmin)


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

xadmin.site.register(Lesson, LessonAdmin)


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']

xadmin.site.register(Video, VideoAdmin)


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']

xadmin.site.register(CourseResource, CourseResourceAdmin)