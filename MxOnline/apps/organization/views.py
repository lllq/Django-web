# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import CityDict, CourseOrg, Teacher
from courses.models import Course
from .forms import UserAskForm
# Create your views here.


class OrgView(View):
    def get(self, request):
        all_citys = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()
        hot_orgs = all_orgs.order_by("-click_nums")[:5]

        city_id = request.GET.get("city", "")
        category = request.GET.get("ct", "")
        sort = request.GET.get("sort", "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        if category:
            all_orgs = all_orgs.filter(category=category)

        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_orgs = all_orgs.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)

        orgs = p.page(page)

        org_nums = all_orgs.count()
        return render(request, "org-list.html", {
            "all_citys": all_citys,
            "org_nums": org_nums,
            "all_orgs": orgs,
            "hot_orgs": hot_orgs,
            "category": category,
            "city_id": city_id,
            "sort": sort,
        })


class UserAskView(View):
    def post(self, request):
        userask_form = UserAskForm()
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail', 'msg':{0}}".format(userask_form.errors), content_type='application/json')


# 机构首页
class OrgHomeView(View):
    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))
        course_org.click_nums += 1
        course_org.save()
        all_courses = course_org.course_set.all()
        all_teaches = course_org.teacher_set.all()

        return render(request, "org-detail-homepage.html", {
            "all_courses": all_courses,
            "all_teachers": all_teaches,
            "course_org": course_org,
            "current_page": current_page,
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = "course"
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_course = course_org.course_set.all()
        return render(request, "org-detail-course.html", {
            "all_course": all_course,
            "course_org": course_org,
            "current_page": current_page,
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = "desc"
        course_org = CourseOrg.objects.get(id=int(org_id))
        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            "current_page": current_page,
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teacher = course_org.teacher_set.all()
        return render(request, "org-detail-teachers.html", {
            "course_org": course_org,
            "all_teacher": all_teacher,
            "current_page": current_page,
        })


# 讲师列表
class TeacherListView(View):
    def get(self, request):
        all_teachers = Teacher.objects.all()
        sort = request.GET.get("sort", "")
        # 人气排序
        if sort:
            all_teachers = all_teachers.order_by("-click_nums")
        # 讲师排行榜
        hot_teachers = all_teachers.order_by("-click_nums")[:3]
        search_keywords = request.GET.get("keywords", "")
        if search_keywords:
            all_teachers = all_teachers.filter(name__icontains=search_keywords)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_teachers, 3, request=request)

        teachers = p.page(page)  # 分页
        teacher_nums = all_teachers.count()
        return render(request, "teachers-list.html", {
            "all_teachers": teachers,
            "teacher_nums": teacher_nums,
            "sort": sort,
            "hot_teachers": hot_teachers,
        })


# 课程详情
class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=int(teacher_id))
        teacher.click_nums +=1
        teacher.save()
        teacher_courses = Course.objects.filter(course_teacher=teacher)
        all_teachers = Teacher.objects.all()
        hot_teachers = all_teachers.order_by("-click_nums")[:3]
        return render(request, "teacher-detail.html", {
            "teacher": teacher,
            "hot_teachers": hot_teachers,
            "teacher_courses": teacher_courses,

        })