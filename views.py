from django.shortcuts import render

# Create your views here.
# trips/views.py

from django.http import HttpResponse
import datetime

def hello_world(request):
     return render(request, 'hello_world.html', {
        'current_time': str(datetime.datetime.now()),
    })
def c0050(request):
    return render(request,'0050.html')
def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })
def Minesweeper(request):
    return render(request,'Minesweeper.html')