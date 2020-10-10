from django.urls import path
from . import views

app_name = "cheeses"

urlpatterns = [
    path("", views.CheeseListView.as_view(), name="list"),
    path("add/", views.CheeseCreateView.as_view(), name="add"),
    path("<slug:slug>/update/", views.CheeseUpdateView.as_view(), name="update"),
    path("<slug:slug>/", views.CheeseDetailView.as_view(), name="detail"),
]
