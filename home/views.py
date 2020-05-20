from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from home.forms import ProfileForm,OsobDocumentForm,DostizhDocumentForm,ZayavlForm
from home.models import Profile,OsobDocument,DostizhDocument
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from home.zayava import writeTextToDoc

def index(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        form = ProfileForm(instance=profile)
        zayavlForm = ZayavlForm(instance=profile)
        OsobFormSet = modelformset_factory(OsobDocument,form=OsobDocumentForm,extra=0)
        DostFormSet = modelformset_factory(DostizhDocument,form=DostizhDocumentForm,extra=0)
        formset1=OsobFormSet(queryset=OsobDocument.objects.filter(profile=profile))
        formset0=DostFormSet(queryset=DostizhDocument.objects.filter(profile=profile))
        return render(request, 'home.html',{
        'form':form,
        'formset0': formset0,
        'formset1': formset1,
        'zayavlForm':zayavlForm,
        })
    else:
        return redirect('log')

def saveDocOsob(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            OsobFormSet = modelformset_factory(OsobDocument,form=OsobDocumentForm,extra=0)
            formset=OsobFormSet(request.POST or None, request.FILES or None)
            if formset.is_valid():
                docfordel=OsobDocument.objects.filter(profile=profile)
                docfordel.delete()
                for form in formset:
                    form.save()
            else:
                    print('blen')

        return redirect('index')


    else:
        return redirect('log')

def saveDocDost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            profile=get_object_or_404(Profile,user=request.user)
            DostFormSet = modelformset_factory(DostizhDocument,form=DostizhDocumentForm,extra=0)
            formset=DostFormSet(request.POST,request.FILES)
            if formset.is_valid():
                print(request.POST)
                docfordel=DostizhDocument.objects.filter(profile=profile)
                docfordel.delete()
                for form in formset:
                    form.save()
            else:
                    print(formset.errors)

        return redirect('index')


    else:
        return redirect('log')

 #выгружаем данные в документ
#формируем список из всех данных и отправляем в скрипт
def saveZayavl(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=ZayavlForm(request.POST or None,request.FILES or None)
            print(request.POST,request.FILES)
            if form.is_valid():
                profile=get_object_or_404(Profile,user=request.user)
                profile.zayavl=request.FILES['zayavl']
                profile.save()
            else:
                print(form.errors)

        return redirect('index')


    else:
        return redirect('log')


def getZayavl(request):

    if request.user.is_authenticated:
            profile=get_object_or_404(Profile,user=request.user)
            data=[]
            doc=writeTextToDoc(listText, firstRow, listFirstTable, secondRow, listSecondTable)
            f =BytesIO()
            doc.save(f)
            response = HttpResponse(f.getvalue(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'inline; filename=plan.docx'
            return response



def saveInfo(request):
    if request.user.is_authenticated:
        profile=get_object_or_404(Profile,user=request.user)
        if request.method=="POST":
            # try:
                form=ProfileForm(request.POST)
                print(request.POST)
                if form.is_valid():
                    newprofile=form.save(commit=False)
                    newprofile.user=request.user
                    newprofile.save()
                    for d in request.POST.getlist('dost'):
                        newdost=DostizhDocument()
                        newdost.type=d
                        newdost.profile=profile
                        newdost.save()
                    for d in request.POST.getlist('osob'):
                        newdost=OsobDocument()
                        newdost.type=d
                        newdost.profile=profile
                        newdost.save()
                        #сохраняет ток послежний, переделать

                else:
                    print(form.errors)
            # except:
            #     return render(request,'error.html',{'content':"Произошла ошибка при сохранении данных"})


        return redirect('index')


    else:
        return redirect('log')
