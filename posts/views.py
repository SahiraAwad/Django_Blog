from django.shortcuts import render
from .models import *

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