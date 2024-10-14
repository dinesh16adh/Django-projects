from django.http import HttpResponse


def aboutUS(request):
    return HttpResponse("hello world this is dinesh adhikari")


def returnfromhome(request):
    return HttpResponse("hello i am returnning from home")


def details(request, detailsid):
    return HttpResponse(detailsid)
