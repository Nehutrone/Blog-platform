from django.http import HttpResponse
from django.shortcuts import render 
from blogs.models import Category,Blog
from assignments.models import About

def home(request):
    categories= Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    # print(featured_post)


#fetch about us 
    try:
        about=About.objects.get()
    except:
        about=None


    context={
        'categories': categories,
        'featured_post':featured_post,
        'posts':posts,
        'about':about
    }
    print(categories)
    return render(request,'home.html',context)



