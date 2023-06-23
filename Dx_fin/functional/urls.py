from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<int:post_id>/', show_post, name='post',),
    path('login/', LoginUser.as_view(), name='login'),
    path('your_template/', city_view),


]