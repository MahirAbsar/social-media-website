from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Follow
from . models import Post,Like
# Create your views here.


@login_required(login_url='sign-in')
def home(request):
    following_list = Follow.objects.filter(follower = request.user)
    post = Post.objects.filter(author__in=following_list.values_list('following'))
    liked_post = Like.objects.filter(user=request.user)
    liked_post_list = liked_post.values_list('post',flat=True)
    if request.method == "GET":
        search = request.GET.get('search')
        if search:
            result = User.objects.filter(username__icontains=search)
        else:
            result = []
    return render(request,'posts/posts.html',{'search':search,'result':result,'following_list':following_list,'liked_post_list':liked_post_list})

@login_required(login_url='sign-in')
def liked(request,pk):
    post = Post.objects.get(pk=pk)

    already_liked = Like.objects.filter(post=post,user = request.user)

    if not already_liked:
        liked_post = Like(post = post,user =request.user)
        liked_post.save()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='sign-in')
def unliked(request,pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post,user = request.user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
