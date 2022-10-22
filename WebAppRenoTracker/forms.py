from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.forms import Form
from .models import newProject
from django.contrib.admin.widgets import AdminDateWidget



class NewProjectForm(forms.ModelForm):
    class Meta:
        model = newProject    
        fields = ('project_title', 'project_start_date',  'house_Level', 'room', 'work_Being_Done', 'price', 'company', 'notes', 'updated_By', 'before_Photo1', 'before_Photo2',
                  'before_Photo3', 'before_Photo4', 'after_Photo1', 'after_Photo2', 'after_Photo3', 'after_Photo4')
        
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
            #'project_start_date': forms.DateField(attrs={'class': 'form-control'}),
            'project_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type': 'date'}),
			'house_Level': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),   
            'work_Being_Done': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'updated_By': forms.Select(attrs={'class': 'form-control'}),
            #'before_Photo1': forms.ImageField(),
            #'before_Photo2': forms.ImageField(),
            #'before_Photo3': forms.ImageField(),
            #'before_Photo4': forms.ImageField(),
            #'after_Photo1': forms.ImageField(),
            #'after_Photo2': forms.ImageField(),
            #'after_Photo3': forms.ImageField(),
            #'after_Photo4': forms.ImageField(),
 
		}



class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = newProject    
        fields = ('project_title','house_Level', 'room', 'work_Being_Done', 'price', 'company', 'notes', 
                  'project_completion_date','after_Photo1', 'after_Photo2', 'after_Photo3', 'after_Photo4')
        
        widgets = {
            'project_title': forms.TextInput(attrs={'class': 'form-control'}),
			'house_Level': forms.TextInput(attrs={'class': 'form-control'}),
            'room': forms.TextInput(attrs={'class': 'form-control'}),   
            'work_Being_Done': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'project_completion_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type': 'date', 'null': 'True'}),
            #'after_Photo1': forms.ImageField(),
            #'after_Photo2': forms.ImageField(),
            #'after_Photo3': forms.ImageField(),
            #'after_Photo4': forms.ImageField(),
 
		}


class SignUpForm(forms.Form):
    pass
    

class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    