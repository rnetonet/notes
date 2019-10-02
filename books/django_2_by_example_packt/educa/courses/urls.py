from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("mine/", views.ManageCourseListView.as_view(), name="manage_course_list"),
    path("create/", views.CourseCreateView.as_view(), name="course_create"),
    path("<pk>/edit/", views.CourseUpdateView.as_view(), name="course_edit"),
    path("<pk>/delete/", views.CourseDeleteView.as_view(), name="course_delete"),
    path("<pk>/module/", views.CourseModuleUpdateView.as_view(), name="course_module_update"),
    path("module/<int:module_id>/content/<str:model_name>/create/", views.ContentUpdateView.as_view(), name="module_content_create"),
    path("module/<int:module_id>/content/<str:model_name>/<id>/", views.ContentUpdateView.as_view(), name="module_content_update"),
    path("content/<int:id>/delete/", views.ContentDeleteView.as_view(), name="module_content_delete"),
    path("module/<int:course_id>/", views.ModuleContentListView.as_view(), name="module_content_list"),
    path("module/order/", views.ModuleOrderChangeView.as_view(), name="module_order"),
    path("module/content/order/", views.ContentOrderChangeView.as_view(), name="content_order"),
    path("", views.CourseListView.as_view(), name="course_list"),
    path("subject/<slug:slug>/", views.CourseListView.as_view(), name="course_list_subject"),
    path("<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail_slug"),
    path("course/detail/<int:pk>/", views.CourseDetailView.as_view(), name="course_detail"),
]