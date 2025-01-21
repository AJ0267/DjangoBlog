from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs
from .forms import AddBlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def get_all_blogs(request):
    blogs = Blogs.objects.all().order_by('-posted_on')
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context=context)


@login_required(login_url='loginuser')
def add_blog(request):
    if request.method == 'POST':
        form = AddBlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('home')
    else:
        form = AddBlogForm()

    context =  {'form': form}
    return render(request, 'blog/blogform.html', context= context)


@login_required(login_url='loginuser')
def get_user_blogs(request):
    blogs = Blogs.objects.filter(user=request.user).order_by('-posted_on')
    context = {'blogs': blogs}
    return render(request, 'blog/userblog.html', context=context)


@login_required(login_url='loginuser')
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id, user=request.user)
    blog.delete()
    return redirect('myblogs')


@login_required(login_url='loginuser')
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id, user=request.user)

    if request.method == 'POST':
        form = AddBlogForm(request.POST, instance=blog)  # form with the existing blog data
        if form.is_valid():
            form.save()  
            return redirect('myblogs') 
    else:
        form = AddBlogForm(instance=blog)

    context = {'form': form, 'blog': blog}
    return render(request, 'blog/edit_blog.html', context)


def view_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    context = {'blog': blog}
    return render(request, 'blog/view_blog.html', context)

