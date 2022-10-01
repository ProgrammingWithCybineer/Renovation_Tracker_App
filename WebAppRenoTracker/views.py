from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.
def index(request):
    return render(request, 'WebAppRenoTracker/index.html')


def home(request):
    return render(request, 'WebAppRenoTracker/home.html')


def currentProjects(request):
    return HttpResponse ("Here is your current project")


def newProject(request):
    return  ("Here is your New project")

def allProjects(request):
    return HttpResponse ("Here is All of your project")

def incompleteProjects(request):
    return HttpResponse ("Here is Incomplete of your project")


def detail(request, id):
    return HttpResponse ("This is the details of your project")

