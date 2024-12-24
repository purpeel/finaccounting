from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model

class AuthPersonForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ['email',
                  'password'
                  ]
        
        
class RegisterPersonForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
    
class PersonUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
