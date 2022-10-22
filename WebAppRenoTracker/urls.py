from django.urls import path
#from . import views
from .views import HomeView, ProjectDetailView, NewProjectView, UpdateProjectView, DeleteProjectView



urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project-details'),
    path('add_new_project/', NewProjectView.as_view(), name= 'new-project'),
    path('projects/update/<int:pk>', UpdateProjectView.as_view(), name= 'update-project'),
    path('projects/<int:pk>/delete', DeleteProjectView.as_view(), name= 'delete-project'),
]

