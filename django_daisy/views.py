from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")


def end_point(request):
    print("hit the end point")
    return HttpResponse()