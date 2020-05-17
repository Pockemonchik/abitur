from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from home.forms import ProfileForm
from home.models import Profile
def index(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        profile.familiya=request.user.username
        form = ProfileForm(instance=profile)
        return render(request, 'home.html',{
        'form':form,
        })
    else:
        return redirect('log')

def saveInfo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            # try:
                form=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
                    newprofile=form.save(commit=False)
                    newprofile.user=request.user
                    newprofile.save()
            # except:
            #     return render(request,'error.html',{'content':"Произошла ошибка при сохранении данных"})

        profile=get_object_or_404(Profile,user=request.user)
        profile.familiya=request.user.username
        form = ProfileForm(instance=profile)
        return render(request, 'home.html',{
        'form':form,
        })
    else:
        return redirect('log')
