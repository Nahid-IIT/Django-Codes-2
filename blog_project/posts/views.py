from django.shortcuts import render, redirect
from posts import forms
from posts.models import Post
def addPost(request):
    if request.method == "POST":
        form = forms.addPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addPost')
    else:
        form=forms.addPost()
    return render(request, 'addPost.html', {'form': form })
        

def editPost(request, id):
    post = Post.objects.get(pk=id)
    form = forms.addPost(instance=post)
    if request.method == "POST":
        form = forms.addPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'addPost.html', {'form': form })    


def deletePost(request , id):
     post = Post.objects.get(pk=id)
     post.delete()
     return redirect('home')