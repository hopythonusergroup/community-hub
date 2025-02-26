from django.shortcuts import render, redirect

from app.models import BlogPost

from app.forms import BlogPostForm


# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "app/blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    post = BlogPost.objects.filter(status="published").get(id=post_id)
    return render(request, "app/blog_detail.html", {"post": post})


def create_blog(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            status = form.cleaned_data["status"]

            print(title, content, status)

            # newblog = {"title": title, "content": content, "status": status}

            newpost = BlogPost(title=title, content=content, status=status)
            newpost.save()  # this actually saves the new post to DB

            # redirect to blog list page
            return redirect("blog_list")
    else:
        form = BlogPostForm()

    return render(request, "app/create_blog.html", {"form": form})
