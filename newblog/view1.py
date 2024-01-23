from django.http import HttpResponse


def salom(request):
    return HttpResponse("Salom Dunyo !... ")


def start_pr(request):
    return HttpResponse("Biz Boshladik !... ")


def start_one(request):
    return HttpResponse("Yangi ish !... ")


def qadam(request):
    return HttpResponse("Ustoz bizga 10 ta view yaratishni aytdilar !... ")


def qadam5(request):
    return HttpResponse("Bu 5 - chi usul !")


def qadam6(request):
    return HttpResponse("Bu 6 - chi usul !")


def qadam7(request):
    return HttpResponse("Bu 7 - chi usul !")


def qadam8(request):
    return HttpResponse("Bu 8 - chi usul !")


def qadam9(request):
    return HttpResponse("Bu 9 - chi usul !")


def qadamend(request):
    return HttpResponse("Bu esa TheEnd oxirgi usul !")
