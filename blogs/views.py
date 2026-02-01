from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.
def posts_by_category(request,category_id):
    # print(category_id)
    # return HttpResponse(category_id)

    #fetch the post that belongs to the category with the id category_id 
    posts=Blog.objects.filter(status='Published',category=category_id)

    #use try and except when we want to do  some custom action if the category does not exist
    try:
        category=Category.objects.get(pk=category_id)   #i want to fetch category 
    except:
        #redirect the user to homepage
        return redirect('home')


    #use get_object_or_404 when you want to show 404 error page if the category does not exists
    # category=get_object_or_404(Category,pk=category_id)     #if you i only get 404 if not exsist

    context={
        'posts':posts,
        'category': category,
    }
    return render(request,'posts_by_category.html',context)


