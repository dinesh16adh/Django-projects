from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        "title": "Home Page",
        "body": "hello i am dinesh adhikair",
        "clist": ["php", "java", "python"],
        "numbers": [10, 20, 30, 40],
        "hello": [],
        "details": [
            {"name": "dinesh adhikari", "location": "pokhara"},
            {"name": "ajit adhikari", "location": "kathmandu"},
        ],
    }
    return render(request, "index.html", data)


def aboutUS(request):
    return HttpResponse("hello world this is dinesh adhikari")


def returnfromhome(request):
    return HttpResponse("hello i am returnning from home")


def details(request, detailsid):
    return HttpResponse(detailsid)
