from django.http import HttpResponse
from django.shortcuts import render


def homeview(request):
    return render(request=request, template_name='index.html', context={})


def end(request):
    return HttpResponse("The end bizning view tugadi !...")
