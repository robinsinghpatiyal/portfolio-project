from django.shortcuts import render

from .models import job

def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})

def jquery1(request):
    return render(request,'jobs/jquery1.html',)

def jquery2(request):
    return render(request,'jobs/jquery2.html',)