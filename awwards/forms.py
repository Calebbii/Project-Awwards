from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project,Profile,Rating

class ProjectPostForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title','description','technologies_used','project_image','repo_link','live_link')

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','bio','location','contact']

class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design_wise', 'usability_wise', 'content_wise']

class Registration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
