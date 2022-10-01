from django.urls import path
#from . import views
from .views import HomeView, ProjectDetailView



urlpatterns = [
    #path('index/', views.index, name="index"),
    #path('', views.home, name="home"),
    #path('currentProjects/', views.currentProjects, name="currentProjects"),
    #path('<int:id>/', views.detail, name="detail"),
    #path('allProjects', views.allProjects, name="allProjects"),
    #path('incompleteProjects', views.incompleteProjects, name="incompleteProjects"),
    #path('newProject', views.newProject, name="newProject"),
    path('',HomeView.as_view(), name='home'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project-details'),
]

