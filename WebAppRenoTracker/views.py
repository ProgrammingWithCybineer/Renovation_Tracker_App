from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import newProject
from .forms import NewProjectForm



# Create your views here.
def index(request):
    return render(request, 'WebAppRenoTracker/index.html')


# def home(request):
    #return render(request, 'WebAppRenoTracker/home.html')

class HomeView(ListView):
    model = newProject
    template_name = 'home.html'


class ProjectDetailView(DetailView):
    model = newProject
    template_name = 'project_details.html'


class NewProject(CreateView):
    model = newProject
    form_class = NewProjectForm
    template_name = 'new_project.html'
    #fields = '__all__'



def currentProjects(request):
    return HttpResponse ("Here is your current project")




def allProjects(request):
    return HttpResponse ("Here is All of your project")

def incompleteProjects(request):
    return HttpResponse ("Here is Incomplete of your project")
