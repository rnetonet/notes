from courses.views import CourseListView
from django.urls import path

from . import views

app_name = "courses"
urlpatterns = [
    path("", views.CourseListView.as_view(), name="course_list"),
    path("create/", views.CourseCreateView.as_view(), name="course_create"),
    path("<pk>/edit/", views.CourseUpdateView.as_view(), name="course_edit"),
    path("<pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete"),
    path("mine/", views.ManageCourseListView.as_view(), name="manage_courses"),
    path(
        "<pk>/modules/", views.CourseModuleUpdateView.as_view(), name="course_modules"
    ),
    path("<pk>/", views.CourseDetailView.as_view(), name="course_detail"),
    path(
        "module/<int:module_id>/content/<model_name>/create/",
        views.ModuleContentManagementView.as_view(),
        name="module_content_create",
    ),
    path(
        "module/<int:module_id>/content/<model_name>/<int:id>/",
        views.ModuleContentManagementView.as_view(),
        name="module_content_edit",
    ),
    path(
        "module/content/<int:id>/delete/",
        views.ContentDeleteView.as_view(),
        name="module_content_delete",
    ),
    path("<slug:subject>/subject/", views.CourseListView.as_view(), name="course_list_by_subject"),
]
