from django.urls import path
from django.views.decorators.cache import cache_page

from students.views import StudentCourseDetailView

from . import views

app_name = "students"
urlpatterns = [
    path(
        "register/",
        views.StudentRegistrationView.as_view(),
        name="student_registration",
    ),
    path("enroll/", views.StudentCourseEnrollView.as_view(), name="student_enroll"),
    path(
        "course/<int:pk>",
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name="student_course_detail",
    ),
    path("courses/", views.StudentCoursesView.as_view(), name="student_courses"),
]
