from django.urls import path
from .views import *

urlpatterns = [
    path('registration_email/', register),
    # path('login/', LoginUser.as_view(), name='login'),
]