from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def projects(request):
    return HttpResponse ("Here is your project")

def projectreno(request, pk):
    return HttpResponse ("Here is your project")