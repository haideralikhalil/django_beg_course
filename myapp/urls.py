from django.urls import path
from . import views

urlpatterns = [
    path("hello", views.hello),
    path("", views.home),
    path("data", views.pass_data),
    path("student", views.student),
    path("liststudents", views.liststudents)
   
]
