# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from DjangoUeditor.models import UEditorField

from django.db import models

from organization.models import CourseOrg, Teacher
# Create your models here.


class Course(models.Model):
    course_teacher = models.ForeignKey(Teacher, verbose_name=u"课程讲师", null=True, blank=True)
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(verbose_name=u"课程", max_length=50)
    desc = models.CharField(verbose_name=u"课程描述", max_length=500)
    detail = UEditorField(verbose_name=u"课程详情", width=600, height=300, imagePath="courses/ueditor/",
                          filePath="courses/ueditor/", default='')
    degree = models.CharField(choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")),
                              max_length=2, default="zj", verbose_name="课程难度" )
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name=u"课程点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    category = models.CharField(default=u"前端开发", max_length=300, verbose_name=u"课程类别")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    tag = models.CharField(default='', verbose_name=u"课程标签", max_length=10)
    youneed_know = models.CharField(verbose_name="课程描述", max_length=300,default='')
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=300,default='')


    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = u"轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def get_video_nums(self):
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, verbose_name=u"访问地址", default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name