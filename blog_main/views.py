from django.http import HttpResponse
from django.shortcuts import render 
from blogs.models import Category,Blog

def home(request):
    categories= Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True).order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    # print(featured_post)

    context={
        'categories': categories,
        'featured_post':featured_post,
        'posts':posts
    }
    print(categories)
    return render(request,'home.html',context)



