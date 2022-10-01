from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import newProject




# Create your views here.
def index(request):
    return render(request, 'WebAppRenoTracker/index.html')


# def home(request):
    #return render(request, 'WebAppRenoTracker/home.html')

class HomeView(ListView):
    model = newProject
    template_name = 'WebAppRenoTracker/home.html'


class ProjectDetailView(DetailView):
    model = newProject
    template_name = 'WebAppRenoTracker/project_details.html'






def currentProjects(request):
    return HttpResponse ("Here is your current project")


def newProject(request):
    return  ("Here is your New project")

def allProjects(request):
    return HttpResponse ("Here is All of your project")

def incompleteProjects(request):
    return HttpResponse ("Here is Incomplete of your project")
