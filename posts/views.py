from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm

# Create your views here.
def post_list(request):

    data = Post.objects.all()
    context={
        'data': data
        }
    return render(request,'posts/post_list.html',context)
    

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)

    context={
        'post': data
        }
    return render(request,'posts/post_detail.html',context)


def create_post(request):



    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
        

    else:
         form = PostForm()



    return render(request,'posts/new.html', {'form':form})



'''
def post_list(request):

    data = Post.objects.all()                              :query
    context={'data': data}                                 :content
    return render(request,'posts/post_list.html',context)  : template
    
'''    

from django.views.generic import ListView , DeleteView

class PostList(ListView):                  # context: post_list, object_list

    model = Post                           #template model_action =post_list

class PostDetail(DeleteView):   # context: post , object
    model = Post                # template name : post_detail(name of model + detail)