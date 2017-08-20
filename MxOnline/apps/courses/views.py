# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Course, Lesson, CourseResource, Video
from operation.models import CourseComments, UserCourse
from  utils.mixin_utils import LoginRequiredMixin
# Create your views here.


# 课程列表
class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "hot":
                all_courses = all_courses.order_by("-click_nums")
            elif sort == "students":
                all_courses = all_courses.order_by("-students")

        hot_courses = all_courses.order_by("-click_nums")[:3]
        search_keywords = request.GET.get("keywords","")
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses,

        })


# 课程详情
class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_nums+=1
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request, "course-detail.html",{
            "course": course,
            "relate_courses": relate_courses
        })


# 课程章节
class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:3]
        all_resources = CourseResource.objects.filter(course=course)

        all_lessons = Lesson.objects.filter(course=course)
        course_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html",{
            "course": course,
            "all_lessons": all_lessons,
            "course_resources": course_resources,
            "relate_courses": relate_courses,
        })


# 课程评论
class CourseCommentView( LoginRequiredMixin,View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_comments = CourseComments.objects.filter(course=course)
        course_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-comment.html",{
            "course": course,
            "all_comments": all_comments,
            "course_resources": course_resources,
        })


# 添加评论
class AddCommentsView(View):
    def post(self, request):
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if course_id >0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


# 课程视频
class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        course.students += 1
        course.save()

        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:3]
        all_resources = CourseResource.objects.filter(course=course)

        all_lessons = Lesson.objects.filter(course=course)
        course_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-play.html",{
            "course": course,
            "all_lessons": all_lessons,
            "course_resources": course_resources,
            "relate_courses": relate_courses,
            "video": video,
        })