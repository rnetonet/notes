from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from .models import Course


def middleware_factory(get_response):
    def middleware(request):
        response = get_response(request)
        return response

    return middleware


class ClassBasedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
