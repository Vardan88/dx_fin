from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from django.db import models
from django_countries.fields import CountryField





class Functional(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    country = CountryField()
    city = models.ForeignKey('City', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Country(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Добро пожаловать!'
        message = f'Здравствуйте, {instance.username}! Спасибо за регистрацию на нашем сайте.'
        recipient_list = [instance.email]

        send_mail(subject, message, DEFAULT_FROM_EMAIL, recipient_list)




from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.user.username