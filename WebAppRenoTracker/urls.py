from django.urls import path
#from . import views
from .views import HomeView, ProjectDetailView, NewProjectView, UpdateProjectView, DeleteProjectView



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
    path('add_new_project/', NewProjectView.as_view(), name= 'new-project'),
    path('projects/update/<int:pk>', UpdateProjectView.as_view(), name= 'update-project'),
    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name= 'delete-project'),
]

