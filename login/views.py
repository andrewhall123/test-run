from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from user_home.models import AccountModel

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password2']
            user.set_password(password)
            user.save()
            new_user=AccountModel.objects.create_account(user=user)
            return redirect('login:account_login')

    form=SignupForm()
    return render(request,'login/signup.html',{'form':form})


def logins(request):
    logout(request)
    error=''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect(reverse('user_home:user_home', kwargs={'user':request.user.username}))
        else:
            error='Please Enter Valid Username and Password'
    form=LoginForm()
    return render(request,'login/login.html', {'form':form,'error':error})



def logouts(request):
    logout(request)
    return HttpResponseRedirect('login:login')
