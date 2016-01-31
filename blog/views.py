from django.shortcuts import render, redirect
from django.utils import timezone
from blog.forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
                form = PostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return render(request, 'blog/post_list.html', {'form': form, 'posts': posts})
                    #return redirect(request, 'blog/post_list.html', {'form': form, 'posts': posts})
    else:
                form = PostForm()
    return render(request, 'blog/post_list.html', {'form': form, 'posts': posts})
