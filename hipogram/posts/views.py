from django.shortcuts import render

from .models import Post


def post_list_view(request):
    posts = Post.objects.all().order_by("-creation_datetime")
    return render(request, "post_list.html", {'posts': posts})
