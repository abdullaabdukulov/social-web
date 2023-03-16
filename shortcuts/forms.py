from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'description']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True})
        }
