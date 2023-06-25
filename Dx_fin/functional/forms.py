# from django import forms
#
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from .models import *
#
# from django_countries.fields import CountryField
# from .models import Country
#
# # class RegisterUserForm(UserCreationForm):
# #     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
# #     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
# #     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
# #     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
# #     languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
# #
# #
# #     class Meta:
# #         model = User
# #         fields = ('languages','username', 'email', 'password1', 'password2')
# #
# #
# #
# # class LoginUserForm(AuthenticationForm):
# #     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
# #     password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#
#
# from django import forms
# from django.core.mail import send_mail
#
# from django import forms
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
#
#
# class RegistrationForm(forms.Form):
#     # Определите поля формы регистрации
#     username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
#
#     email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
#     languages = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))
#
#     def send_registration_email(self, email):
#         subject = 'Регистрация прошла успешно'
#         message = render_to_string('functional/registration_email.html')  # Загрузка и рендеринг HTML-шаблона письма
#         from_email = 'gurgentadevosyan66@gmail.com'  # Адрес отправителя
#         recipient_list = [email]  # Адрес получателя(ей)
#
#         send_mail(subject, message, from_email, recipient_list, html_message=message)
#
#     def send_registration_email(self, email):
#         # Загрузка и рендеринг HTML-шаблона письма
#         message = render_to_string('functional/registration_email.html')
#
#         # Отправка письма

from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()





