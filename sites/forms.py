from django import forms
from .models import Project,Profile,Rate

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['date','user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design','usability','content']