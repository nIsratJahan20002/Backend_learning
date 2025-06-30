from django.shortcuts import render, redirect

from .models import Blog
from .forms import BlogForm


def index(request):
    context = {
        "blogs": Blog.objects.all().order_by("title"),
    }
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("/")
    else:
        blog_form = BlogForm()

    context = {
        "form": blog_form,
    }
    return render(request, "blog_form.html", context)


def update(request, id):
    specific_blog = Blog.objects.get(id=id)

    if request.method == "POST":
        blog_form = BlogForm(request.POST, instance=specific_blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect("/")
    else:
        blog_form = BlogForm(instance=specific_blog)

    context = {
        "form": blog_form,
    }
    return render(request, "blog_form.html", context)


def delete(request, id):
    specific_blog = Blog.objects.get(id=id)
    specific_blog.delete()
    return redirect("blog_list")
