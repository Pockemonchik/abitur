from django.shortcuts import render,reverse,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserLoginForm,UserRegisterForm
from django.contrib.auth import logout
from home.models import Profile
from django.contrib.auth.models import User

# Create your views here.
def log(request):
    form=UserLoginForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request,'error.html',{'content':"Введены неверные данные, попробуйте снова"})

    else:
        form=UserLoginForm()
        regform=UserRegisterForm()
        return render(request, 'login.html',{'form': form,'regform':regform})

def reg(request):
    regform=UserRegisterForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if regform.is_valid():
            # try:
                 newuser =User.objects.create_user(regform.cleaned_data.get('username'),None,regform.cleaned_data.get('password'))

                 newuser.save()
                 profile = Profile()
                 profile.user=newuser
                 profile.nomer=request.POST.get('password')
                 profile.familiya=newuser.username
                 newuser.save()
                 profile.save()
                 login(request,newuser)
                 return HttpResponseRedirect(reverse('index'))
            # except:
                 # return render(request,'error.html',{'content':"Произошла ошибка при регистрации"})

        else:
            print(regform.errors)
            return render(request,'error.html',{'content':"Произошла ошибка при регистрации, ошибка в форме"})


    else:
        form=UserLoginForm()
        regform=UserRegisterForm()
        return render(request, 'login.html',{'form': form,'regform':regform})


def logout_view(request):
    logout(request)
    return redirect('log')
