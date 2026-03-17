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


def blogs(request,slug):
    single_blog= get_object_or_404(Blog,slug=slug,status='Published')
    context= {
        'single_blog':single_blog
    }
    return render(request,'blogs.html',context)




def search(request):
    keyword=request.GET.get('keyword')
    # print('keywrd==>',keyword)
    blogs=Blog.objects.filter(title__icontains=keyword,status='Published')   #fetch the blog post whose title contains the keyword that user has searched for
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request,'search.html')


