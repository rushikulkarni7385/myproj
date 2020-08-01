from django.shortcuts import render
from testapp.models import *
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpform,HydJobsform,ChennaiJobsform,PuneJobsform,BangloreJobsform
from django.http import HttpResponseRedirect
# Create your views here.


def homepage(request):
    return render(request,'index.html')

@login_required()
def hyd_Jobs(request):
    h=Hyd_Jobs.objects.all()
    return render(request,'Hyd_Jobs.html',{'h':h})

@login_required()
def banglore_Jobs(request):
    b=Banglore_Jobs.objects.all()
    return render(request,'Banglore_Jobs.html',{'b':b})

@login_required()
def pune_Jobs(request):
    p=Pune_Jobs.objects.all()
    return render(request,'Pune_Jobs.html',{'p':p})

@login_required()
def chennai_Jobs(request):
    c=Chennai_Jobs.objects.all()
    return render(request,'Chennai_Jobs.html',{'c':c})

def logout_view(request):
    return render(request,'logout.html')

def signup_view(request):
    form=SignUpform()
    if request.method=='POST':
            form=SignUpform(request.POST)
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login/")
    return render(request,'signup.html',{'form':form})

def Posthydjobs_view(request):
    form=HydJobsform()
    if request.method=='POST':
        form=HydJobsform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'posthydjobs.html',{'form':form})

def PostChennaijobs_view(request):
    form=ChennaiJobsform()
    if request.method=='POST':
        form=ChennaiJobsform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'postchennaijobs.html',{'form':form})

def PostPunejobs_view(request):
    form=PuneJobsform()
    if request.method=='POST':
        form=PuneJobsform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'postpunejobs.html',{'form':form})

def PostBanglorejobs_view(request):
    form=BangloreJobsform()
    if request.method=='POST':
        form=BangloreJobsform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'postbanglorejobs.html',{'form':form})

def postjob_view(request):
    return render(request,'postjobs.html')

def thanku_view(request):
    return render(request,'thanku.html')

def about_view(request):
    return render(request,'about.html')