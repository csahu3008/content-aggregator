from django.shortcuts import render,get_object_or_404,get_list_or_404,HttpResponse,redirect
from django.urls import reverse_lazy,reverse
from .models import Category,Comment,News
from django.http import JsonResponse
import requests
import json
from django.db.models import Q
from django.views.generic import ListView
from django.core import files
from .forms import inputForm,CommentForm,newsform
from PIL import Image
from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib.request
import random
import os
from django.contrib.auth.decorators  import login_required
import re
from django.views.generic import CreateView,UpdateView,TemplateView,DeleteView
# Create your views here.
c=1
def AddNews(request):
    if request.method=='POST':
        form=newsform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            status='success'
        else:
            status='failure'

        data={'status':status}
        return JsonResponse(data)
    else:
        form=newsform()
    return render(request,'add.html',{'form':form})
@login_required
def dislikes_add(request,id):
    news=News.objects.get(id=id)
    user=request.user
    if request.user.is_authenticated:
        if request.user not in news.dislikes.all():
            if request.user not in news.likes.all():
                news.dislikes.add(user)
            else:
                news.dislikes.add(user)
                news.likes.remove(user)
        else:
            news.dislikes.remove(user)
        use=news.likes.count()
        use1=news.dislikes.count()

        data={'liked':'True','total':use,'dtotal':use1}
        return JsonResponse(data)
    else:
        return redirect('/users/login/')
@login_required
def likes_add(request,id):
    news=News.objects.get(id=id)
    user=request.user
    if request.user.is_authenticated:
        if request.user not in news.likes.all():
            if request.user not in news.dislikes.all():
                news.likes.add(user)
            else:
                news.likes.add(user)
                news.dislikes.remove(user)
        else:
            news.likes.remove(user)
        use=news.likes.count()
        use1=news.dislikes.count()

        data={'liked':'True','total':use,'dtotal':use1}
        return JsonResponse(data)
    else:
        return redirect('/users/login/')

def ListNews(request,new_context={}):
    list=get_list_or_404(News)
    context={'list':list}
    context.update(new_context)
    return render(request,'list.html',context)

def SearchResults(request):
    api_key=os.environ.get('NEWS_API')
    title=request.GET.get('q')
    url="https://newsapi.org/v2/everything?q={}&apiKey={}".format(title,api_key)
    p=requests.get(url)
    n=p.json()
    list1=[]
    for m in n['articles']:
        headline=m['title']
        author=m['author']
        des=str(m['content'])
        p=re.compile('\[\+[\d\w\s]*\]')
        des=p.sub('',des)
        url=m['url']
        url_img=m['urlToImage']
        context={'headline':headline,'url_img':url_img,'url':url,'des':des,'date_published':m['publishedAt']}
        list1.append(context)
    # template_name='search_list.html'
    # def get_queryset(self):
    #     query=self.request.GET.get('q')
    #     list=News.objects.filter(Q(headline__icontains=query)|Q(description__icontains=query))
    #     return list
    return render(request,'search_list.html',{'list':list1})

def DetailNews(request,id):
    news=get_object_or_404(News,id=id)
    if request.method=='POST':
        if request.user.is_authenticated:
                status=1
        else:
                status=0
                url='/users/login/'
        if status==0:
            data={'status':status,'message':'You need to login first','url':url}
            return JsonResponse(data)
        form=CommentForm(request.POST)
        comment=form.save()
        comment.user=request.user
        comment.news=news
        comment.save()
        if status==1:
            data={'status':status,'message':'your comment was added successfully'}
            return JsonResponse(data)
    else:
        form=CommentForm()
    c=Comment.objects.all()
    context={'news':news,'form':form,'c':c}
    return render(request,'news_detail.html',context)

def category(request,category):
    n=Category.objects.get(title=category)
    list=n.news_set.all()
    context={'list':list}
    return render(request,'category.html',context)

def ContentUpdator(request):
    global c
    if c == 1:
        category="general"
        c+=1
    elif c==2:
        category="science"
        c+=1
    elif c==3:
        category="sports"
        c+=1
    elif c==4:
        category="health"
        c+=1
    elif c==5:
        category="technology"
        c+=1
    elif c==6:
        category="entertainment"
        c+=1
    elif c==7:
        category="business"
        c=1
    api_key=os.environ.get('NEWS_API')
    url="https://newsapi.org/v2/top-headlines?country=in&category={}&pagesize=50&apiKey={}".format(category,api_key)
    p=requests.get(url)
    n=p.json()
    for m in n['articles']:
        try:
            headline=m['title']
            p=re.findall(r'-\s[\w\s]*',headline)
            p=p[-1]
            headline=re.compile(p).sub('',headline)
            if(News.objects.filter(headline=headline).exists()):
                pass
            else: 
                author=m['author']
                des=str(m['content'])
                p=re.compile('\[\+[\d\w\s]*\]')
                des=p.sub('',des)
                url=m['url']
                url_img=m['urlToImage']
                topic=Category.objects.get(title=category)
                u=News.objects.create(headline=headline,description=des,url=url,url_image=url_img,author=author,)
                u.categories.add(topic)
                regex = re.compile(r'^(?:http|ftp)s?://'r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'r'localhost|'r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'r'(?::\d+)?'r'(?:/?|[/?]\S+)$', re.IGNORECASE)
                if url_img is None:
                    print('Url is empty')
                else:            
                    if url_img is not None:
                        img_result=requests.get(url_img)
                        fp = BytesIO()
                        fp.write(img_result.content)
                        file_name =str(random.random()*1000)+'.jpg'
                        u.picture.save(file_name, files.File(fp))
                    u.save()
        except AttributeError or OperationalError or NewConnectionError:
                pass
    data={'status':'success'}
    return JsonResponse(data)


def wheather(request):
    api_key=os.environ.get('openweather_api')
    title=request.GET.get('place')
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(title,api_key)
    print(title)
    n=requests.get(url).json()
    current_temp=round(n['main']['temp']-273,2)
    max_temp=round(n['main']['temp_max']-273,2)
    min_temp=round(n['main']['temp_min']-273,2)
    humidity=n['main']['humidity']
    data={'place':title,'current_temp':current_temp,'max_temp':max_temp,'min_temp':min_temp,'humidity':humidity}
    print(data)
    context={'data':data}
    response=ListNews(request,context)
    return response