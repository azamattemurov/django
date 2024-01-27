from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def homeview(request):
    print(str(request))
    context = {"dushanba": ("matematika", "rustili", "onatili", "___", "fizika", "jismoniy"),
               "seshanba": ("matematika", "rustili", "onatili", "___", "fizika", "jismoniy"),
               "chorshanba": ("matematika", "rustili", "onatili", "___", "fizika", "jismoniy"),
               "payshanba": ("matematika", "rustili", "onatili", "___", "fizika", "jismoniy")}
    return render(request=request, template_name='index.html', context={'context':context})



def end(request):
    print(str(request))
    return render(request=request,template_name='home.html',context={})
