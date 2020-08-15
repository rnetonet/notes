from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import forms
from courses import models as courses_models

# Create your views here.
class StudentRegistrationView(CreateView):
    template_name = "students/student/registration.html"
    form_class = UserCreationForm
    # success_url = reverse_lazy("students:student_course_list")
    success_url = reverse_lazy("courses:course_list")
    
    def form_valid(self, form):
        result = super().form_valid(form)

        # Register and authenticate
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password1"])
        login(self.request, user)

        return result

class StudentCourseEnrollView(LoginRequiredMixin, FormView):
    course = None
    form_class = forms.CourseEnrollForm
    template_name = "students/student/enroll.html"

    def form_valid(self, form):
        self.course = form.cleaned_data["course"]
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("students:student_courses")

class StudentCoursesView(ListView):
    template_name = "students/student/courses.html"

    def get_queryset(self):
        return self.request.user.courses_joined.all()

class StudentCourseDetailView(DetailView):
    model = courses_models.Course
    template_name = "students/student/course_detail.html"