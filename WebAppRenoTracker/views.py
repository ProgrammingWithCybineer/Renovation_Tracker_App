from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import newProject
from .forms import NewProjectForm, UpdateProjectForm



# Create your views here.
def index(request):
    return render(request, 'WebAppRenoTracker/index.html')


# def home(request):
    #return render(request, 'WebAppRenoTracker/home.html')

class HomeView(ListView):
    model = newProject
    template_name = 'home.html'
    ordering = ['project_start_date'] # will change to date field later


class ProjectDetailView(DetailView):
    model = newProject
    template_name = 'project_details.html'


class NewProjectView(CreateView):
    model = newProject
    form_class = NewProjectForm
    template_name = 'new_project.html'
    #fields = '__all__'


class UpdateProjectView(UpdateView):
    model = newProject
    form_class = UpdateProjectForm  
    template_name = 'update_project.html'
    #fields = ['project_title', 'house_Level', 'room', 'work_Being_Done', 'price', 'company', 'notes',
    #            'after_Photo1', 'after_Photo2', 'after_Photo3', 'after_Photo4']


class DeleteProjectView(DeleteView):
    model = newProject
    template_name = 'delete_project.html'
    success_url = reverse_lazy('home') # might change to a successfully deleted messaged later









# def currentProjects(request):
    #return HttpResponse ("Here is your current project")


# def allProjects(request):
    #return HttpResponse ("Here is All of your project")

# def incompleteProjects(request):
    #return HttpResponse ("Here is Incomplete of your project")
