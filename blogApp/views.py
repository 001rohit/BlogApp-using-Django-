from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from .models import blogApp
def home(request):
    blog = blogApp.objects.all()
    context={
          'blog':blog,
     }
    return render(request,'BlogList.html',context)

def blog_list(request):
    blog = blogApp.objects.all()
    check = blog[::1]
    context={
        'blog':check,
    }
    return render(request,'addBlog.html',context)

def more(request,pk):
    blog1 = get_object_or_404(blogApp,pk=pk)
    context = {
        'blog1':blog1,
    }
    return render(request,'more.html',context)    

def add_blog(request):
    if request.method=='POST':
        data = request.POST.dict()
        img = request.FILES.get('img')

        blogApp.objects.create(title=data['title'],img=img,desc = data['desc'])
        return redirect('blog_list')
    
    else:
        return render(request,'addBlog.html')
    
def home1(request):
    return redirect('home')

def remove(request,pk):
    blog = get_object_or_404(blogApp,pk=pk)
    blog.delete()
    return redirect('home')

def editBlog(request,pk):
    get_blog = get_object_or_404(blogApp,pk=pk)
    print(get_blog.title)
    if request.method =='POST':
        new_title = request.POST['title']
        new_desc = request.POST['desc']
        new_img = request.FILES.get('img')
        # print(new_title)
        # print(new_img)
        get_blog.title=new_title
        get_blog.desc=new_desc
        get_blog.img=new_img
        get_blog.save()
        return redirect('home')
    
    else:
        context={
            'get_blog':get_blog,
        }
        return render(request,'edit_task.html',context)

        