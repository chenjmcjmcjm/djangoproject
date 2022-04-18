
from django.shortcuts import render
from django.views.decorators import csrf


def cal0050(request):
    ctx = {}
    if request.POST:
        ctx['showstart'] = request.POST['starttime']
        ctx['showend'] = request.POST['endtime']
    return render(request, "0050.html", ctx)
