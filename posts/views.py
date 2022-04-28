from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Follow
# Create your views here.


@login_required(login_url='sign-in')
def home(request):
    following_list = Follow.objects.filter(follower = request.user)
    if request.method == "GET":
        search = request.GET.get('search')
        if search:
            result = User.objects.filter(username__icontains=search)
        else:
            result = []
    return render(request,'posts/posts.html',{'search':search,'result':result,'following_list':following_list})
