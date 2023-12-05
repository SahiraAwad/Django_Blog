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

def edit_post(request,pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
        

    else:
         form = PostForm(instance= post)

    return render(request,'posts/edit.html', {'form':form})

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')
'''
def post_list(request):

    data = Post.objects.all()                              :query
    context={'data': data}                                 :content
    return render(request,'posts/post_list.html',context)  : template
    
'''    

from django.views.generic import ListView , DeleteView , CreateView, UpdateView, DetailView

class PostList(ListView):                  # context: post_list, object_list

    model = Post                           #template model_action =post_list

class PostDetail(DeleteView):   # context: post , object
    model = Post                # template name : post_detail(name of model + detail)


class AddPost(CreateView):
    model=Post
    fields = '__all__'   
    success_url = '/posts/'

class EditPost(UpdateView):
    model=Post
    fields = '__all__'   
  
    template_name = 'posts/edit.html'   

class DeletePost(DeleteView):
    model= Post 
    success_url = '/posts/' 





