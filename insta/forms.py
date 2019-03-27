from django import forms
from .models import Image, Profile

class AddPicForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'likes', 'user', 'profile']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }