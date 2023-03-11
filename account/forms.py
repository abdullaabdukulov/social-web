from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password(self):
        if not self.cleaned_data['password']:
            raise forms.ValidationError("Enter a password.")
        return self.cleaned_data['password']

    def clean_password2(self):
        if not self.cleaned_data['password2']:
            raise forms.ValidationError("Enter your password (again)")
        return self.cleaned_data['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use!')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(pk=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use!')
        return data


class UserProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = UserProfile
        fields = ['date_of_birth', 'photo']
