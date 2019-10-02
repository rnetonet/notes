from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from students.forms import CourseEnrollForm

from .forms import ModuleFormSet
from .models import Content, Course, Module, Subject


class CourseListView(TemplateView):
    template_name = "courses/course/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        subjects = Subject.objects.annotate(total_courses=Count("courses"))
        courses = Course.objects.annotate(total_modules=Count("modules"))

        if kwargs.get("slug"):
            subject = get_object_or_404(Subject, slug=kwargs.get("slug"))
            courses = courses.filter(subject=subject)

            context["subject"] = subject

        context["subjects"] = subjects
        context["courses"] = courses

        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course/detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context["enroll_form"] = CourseEnrollForm(initial={"course": self.object})
        return context


class ContentOrderChangeView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for id, order in self.request_json.items():
            Content.objects.get(id=id, module__course__owner=request.user).update(
                order=order
            )
        return self.render_json_response({"saved": "OK"})


class ModuleOrderChangeView(CsrfExemptMixin, JsonRequestResponseMixin, View):
    def post(self, request):
        for id, order in self.request_json.items():
            Module.objects.get(id=id, course__owner=request.user).update(order=order)
        return self.render_json_response({"saved": "OK"})


class ContentUpdateView(TemplateResponseMixin, View):
    module = None
    model = None
    obj = None
    template_name = "courses/manage/content/form.html"

    def get_model(self, model_name):
        if model_name in ("textitem", "image", "video", "file"):
            return apps.get_model(app_label="courses", model_name=model_name)
        return None

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

        return super(ContentUpdateView, self).dispatch(
            request, module_id, model_name, id
        )

    def get(self, request, module_id, model_name, id=None):
        form = self.get_form(self.get_model(model_name), instance=self.obj)
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

            return redirect("courses:module_content_list", self.module.course.id)

        return self.render_to_response({"form": form, "object": self.obj})


class ContentDeleteView(View):
    def post(self, request, id):
        content = get_object_or_404(Content, id=id, module__course__owner=request.user)

        module = content.module

        content.item.delete()
        content.delete()

        return redirect("courses:module_content_list", module.course.id)


class ModuleContentListView(TemplateResponseMixin, View):
    template_name = "courses/manage/module/content_list.html"

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id, owner=request.user)
        return self.render_to_response({"course": course})


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
            return redirect("courses:manage_course_list")
        return self.render_to_response({"course": self.course, "formset": formset})


class OwnerMixin:
    """
    Restrict queryset to those owned by user.
    """

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    """
    If filled form is valid, set the user in the model instance.
    """

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin, LoginRequiredMixin, SuccessMessageMixin):
    """
    Define the model as Course and restrict the queryset (inheritance) to
    those owned by request.user.
    """

    model = Course
    fields = ("subject", "title", "slug", "overview")
    success_url = reverse_lazy("courses:manage_course_list")
    success_message = "Action successfully executed"


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    """
    Basic configuration to Create and Update views.
    """

    fields = ("subject", "title", "slug", "overview")
    success_url = reverse_lazy("courses:manage_course_list")
    template_name = "courses/manage/course/form.html"


class ManageCourseListView(OwnerCourseMixin, OwnerMixin, ListView):
    """
    List the courses managed by request.user.
    """

    template_name = "courses/manage/course/list.html"


class CourseCreateView(PermissionRequiredMixin, OwnerCourseEditMixin, CreateView):
    permission_required = "courses.add_course"


class CourseUpdateView(PermissionRequiredMixin, OwnerCourseEditMixin, UpdateView):
    permission_required = "courses.change_course"


class CourseDeleteView(PermissionRequiredMixin, OwnerCourseMixin, DeleteView):
    permission_required = "courses.delete_course"
    template_name = "courses/manage/course/delete.html"
    success_url = reverse_lazy("courses:manage_course_list")
