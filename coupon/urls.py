from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("create/", views.register, name="register"),
    path("user", views.user_details, name="user"),
]
