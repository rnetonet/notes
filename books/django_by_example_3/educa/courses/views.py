from typing import List

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import ModuleFormSet
from .models import Content, Course, Module, Subject


class OwnerQuerysetFilterMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerFormFillMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CourseViewMixin(
    OwnerQuerysetFilterMixin, LoginRequiredMixin, PermissionRequiredMixin
):
    model = Course
    fields = ["subject", "title", "slug", "overview"]
    success_url = reverse_lazy("courses:manage_courses")


class CourseEditViewMixin(CourseViewMixin, OwnerFormFillMixin):
    template_name = "courses/course/form.html"


class ManageCourseListView(CourseViewMixin, ListView):
    template_name = "courses/course/mine.html"
    permission_required = "courses.view_course"


class CourseCreateView(CourseEditViewMixin, CreateView):
    permission_required = "courses.add_course"


class CourseUpdateView(CourseEditViewMixin, UpdateView):
    permission_required = "courses.change_course"


class CourseDeleteView(CourseViewMixin, DeleteView):
    template_name = "courses/course/delete.html"
    permission_required = "courses.delete_course"


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = "courses/manage/module/formset.html"
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)

    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({"course": self.course, "formset": formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("courses:manage_courses")
        return self.render_to_response({"course": self.course, "formset": formset})


class ModuleContentManagementView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = "courses/manage/content/form.html"

    def get_model(self, model_name):
        if model_name in ("text", "video", "image", "file"):
            return apps.get_model("courses", model_name)

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(
            model, exclude=["owner", "order", "created", "updated"]
        )
        return Form(*args, **kwargs)

    def dispatch(self, request, module_id, model_name, id=None):
        self.module = get_object_or_404(
            Module, id=module_id, course__owner=request.user
        )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(self.model, id=id, owner=request.user)
        return super().dispatch(request, module_id, model_name, id)

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response({"form": form, "object": self.obj})

    def post(self, request, module_id, model_name, id=None):
        form = self.get_form(
            self.model, instance=self.obj, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            if not id:
                Content.objects.create(module=self.module, item=obj)
            return redirect("courses:course_detail", self.module.course.id)


class CourseDetailView(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    permission_required = [
        "courses.create_module",
        "courses.change_module",
        "courses.delete_module",
    ]
    template_name = "courses/course/detail.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class ContentDeleteView(View, LoginRequiredMixin, PermissionRequiredMixin):
    def post(self, request, id):
        content = get_object_or_404(
            Content, id=id, module__course__owner=self.request.user
        )

        course_id = content.module.course.id

        content.item.delete()
        content.delete()
        return redirect("courses:course_detail", course_id)

class CourseListView(ListView):
    model = Course
    template_name = "courses/course/list.html"

    subject = None

    def dispatch(self, request, *args, **kwargs):
        if "subject" in self.kwargs:
            self.subject = Subject.objects.get(slug=self.kwargs["subject"])

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        
        qs = qs.annotate(total_modules=Count("modules"))

        if self.subject:
            qs = qs.filter(subject=self.subject)
        return qs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["subjects"] = Subject.objects.annotate(total_courses=Count("courses"))
        context_data["subject"] = self.subject

        return context_data