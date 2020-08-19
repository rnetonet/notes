from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from courses.models import Course

# Create your views here.
class CourseChatRoomView(LoginRequiredMixin, DetailView):
    template_name = "chat/room.html"

    def get_queryset(self):
        return self.request.user.courses_joined.all()