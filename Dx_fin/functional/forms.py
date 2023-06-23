from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

from django_countries.fields import CountryField
from .models import Country

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
    # country = forms.ModelChoiceField(queryset=Country.objects.all(), empty_label=None)
    # city = forms.ModelChoiceField(queryset=City.objects.none(), empty_label=None)
    # country = CountryField().formfield()
    # country_code = forms.CharField(max_length=3)
    # birth_date = forms.DateField(label='Дата рождения')
    # age = forms.IntegerField(label='Возраст')

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #
    #     # Остальной код сохранения User
    #
    #     if commit:
    #         user.save()
    #         UserProfile.objects.create(
    #             user=user,
    #             country=self.cleaned_data['country'],
    #             city=self.cleaned_data['city'],
    #             birth_date=self.cleaned_data['birth_date'],
    #             age=self.cleaned_data['age']
    #         )
        # return user

    class Meta:
        model = User
        fields = ('languages','username', 'email', 'password1', 'password2')



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))










