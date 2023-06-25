# import email
#
# from django.contrib.auth import logout, login
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.views import LoginView
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from .send_email import send_registration_email
#
# from .forms import *
#
# from .models import *
# from .sms_utils import send_sms
#
# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'functional/register.html'
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')
#
#     def register(request):
#         # Логика регистрации пользователя
#         # ...
#
#         # Отправка письма при регистрации
#         send_registration_email(email)
#
#         return render(request, 'registration_complete.html')
#
#
#
#
# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'functional/login.html'
#
#     def get_success_url(self):
#         return reverse_lazy('home')
#
# def logout_user(request):
#     logout(request)
#     return redirect('login')

# from django.shortcuts import render
# from .forms import RegistrationForm
# from django.core.mail import send_mail
#
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             # Обработка регистрации и сохранение пользователя в базе данных
#
#
#
#             # Отправка электронной почты
#
#
#             form.send_registration_email(email)
#
#             # Вернуть ответ пользователю о успешной регистрации или перенаправить на другую страницу
#             return render(request, 'functional/registration_email.html')
#     else:
#         form = RegistrationForm()
#
#     return render(request, 'functional/registration_email.html', {'form': form})
#
#
#
# # class RegisterUser(CreateView):
# # #     form_class = RegisterUserForm
# # #     template_name = 'functional/register.html'
# # #     success_url = reverse_lazy('login')
# # #
# # #     def form_valid(self, form):
# # #         user = form.save()
# # #         login(self.request, user)
# # #         return redirect('home')


from django.shortcuts import render
from django.core.mail import send_mail
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Обработка регистрации и сохранение пользователя в базе данных

            # Отправка электронной почты
            email = form.cleaned_data['email']
            send_mail(
                'Подтверждение регистрации',
                'Добро пожаловать! Ваша регистрация прошла успешно.',
                'gurgentadevosyan@mail.ru',  # Адрес отправителя
                [email],  # Адрес получателя
                fail_silently=False,
            )

            # Вернуть ответ пользователю о успешной регистрации или перенаправить на другую страницу
            return render(request, 'functional/registration_email.html')
    else:
        form = RegistrationForm()

    return render(request, 'functional/registration_email.html', {'form': form})



