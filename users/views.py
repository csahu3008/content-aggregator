from django.shortcuts import render,redirect,HttpResponse,reverse
from django.contrib.auth import login,authenticate
from django.views.generic import FormView
from .models import MyUser
from .forms import MyUserForm,loginform
# Create your views here.
def signup(request):
    if(request.method=='POST'):
        form=MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            cd=form.cleaned_data['name']
            request.session['cookie']=cd
            context={'form':form,'cook':request.session.get('cookie','hello')}
            return render(request,'registration/signup_done.html',context)
        
    else:
        form=MyUserForm()
    return render(request,'registration/signup.html',{'form':form})


def Login(request):
    if request.session.get('mobile') or request.session.get('email'):
        return redirect(reverse('list'))
    else:
        if request.method=='POST':
            form=loginform(request.POST)
            if form.is_valid():
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                mobile=form.cleaned_data['mobile']
                user=authenticate(request,mobile=mobile,email=email,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        request.session['email']=email
                        request.session['mobile']=mobile
                        return redirect(reverse('list'))
                    else:
                        return HttpResponse('you are not active user')
                else:
                    return HttpResponse('Your account is not found')
            else:
                return HttpResponse('your login details are invalid')
        else:
            form=loginform()
        return render(request,'registration/login.html',{'form':form})

