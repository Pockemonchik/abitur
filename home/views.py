from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.db.models import Q
def index(request):
    if request.user.is_authenticated:
        return render(request, 'home.html',{
        })
    else:
        return redirect('log')
