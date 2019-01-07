
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from user.models import new_feed
import datetime

class index(ListView):
    template_name="user/index.html"

    def get(self,request):
        all_feeds=new_feed.objects.all()
        return render(request,self.template_name,{"all_feeds":all_feeds})

    def post(self,request):
        text=request.POST.get('all_feeds')
        date=datetime.datetime.now()
        name=request.user.username
        p=new_feed(name=name,data=text,date=date)
        print(p)
        p.save()

        all_feeds = new_feed.objects.all()
        return render(request,self.template_name,{"all_feeds":all_feeds})


class user(DetailView):
    template_name='user/user_feeds.html'
    def get(self,request):
        user_feeds=new_feed.objects.filter(name=request.user.username)
        return render(request,self.template_name,{'user_feeds':user_feeds})


class search(ListView):
    template_name='user/search.html'

    def get(self,request):
        return render(request,self.template_name,{'post':False})

    def post(self,request):
        query=request.POST.get('q')
        if User.objects.filter(username=query).exists():
            return render(request,self.template_name,{'user_found':True,'query':query,'post':True})
        else:
            return render(request,self.template_name,{'user_found':False,'query':query,'post':True})

class about(ListView):
    template_name='user/about.html'
    def get(self,request):
        return render(request,self.template_name)

class othersfeed(ListView):
    template_name='user/othersfeed.html'

    def get(self,request):
        user=request.GET.get('othersfeed')
        feed=new_feed.objects.filter(name=user)
        return render(request,self.template_name,{'feed':feed,'user':user})
