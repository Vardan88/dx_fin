import email

from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .send_email import send_registration_email

from .forms import *

from .models import *




def show_post(request, post_id):
    return HttpResponse (f"Отображение статьи с id = {post_id}" )





class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'functional/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def register(request):
        # Логика регистрации пользователя
        # ...

        # Отправка письма при регистрации
        send_registration_email(email)

        return render(request, 'registration_complete.html')





class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'functional/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


from django.shortcuts import render
from .forms import RegisterUserForm
from .models import Country, City

from django.shortcuts import render
from .forms import RegisterUserForm

def city_view(request):
    form = RegisterUserForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

    return render(request, 'functional/your_template.html', {'form': form})








