from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import PostForm
from .models import Answer, Post
# Create your views here.


def first_html_response(request):
    html = '<html><body>It is now %s.</body></html>'
    return HttpResponse(html)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    url_address = str(post.url_address)
    url_address.split("/")
    post.url_address_second = url_address[0]
    return render(request, 'changer/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'changer/post_edit.html', {'form': form})


def post_list(request):
    return render(request, 'changer/post_list.html', {})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'changer/post_edit.html', {'form': form})
