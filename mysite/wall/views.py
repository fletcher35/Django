from django.shortcuts import render, get_object_or_404
from wall.models import *
from django.contrib.auth.models import *

def detail(request,pk):
    user = get_object_or_404(User,pk=pk)
    wall_messages_list = Message.objects.filter(taker=user).order_by('-datetime')[:5]
    return render(request,'detail.html',{'user':user, 'wall_messages_list':wall_messages_list})
