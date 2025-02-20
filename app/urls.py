from django.urls import path

from app.views import blog_list

urlpatterns = [
    path("", blog_list, name="blog_list"),
]
