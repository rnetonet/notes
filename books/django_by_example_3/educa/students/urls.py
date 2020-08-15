from django.urls import path

from . import views

app_name = "students"
urlpatterns = [
    path(
        "register/",
        views.StudentRegistrationView.as_view(),
        name="student_registration",
    ),
    path(
        "enroll/",
        views.StudentCourseEnrollView.as_view(),
        name="student_enroll"
    ),
    path(
        "courses/",
        views.StudentCoursesView.as_view(),
        name="student_courses"
    )
]
