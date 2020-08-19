from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
    path("room/<pk>/", views.CourseChatRoomView.as_view(), name="course_chat_room")
]
