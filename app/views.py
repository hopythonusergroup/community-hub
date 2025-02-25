from django.shortcuts import render

from app.models import BlogPost


# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "app/blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    post = BlogPost.objects.filter(status="published").get(id=post_id)
    return render(request, "app/blog_detail.html", {"post": post})
