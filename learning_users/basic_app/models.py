from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user tem os seguintes atributos => https://docs.djangoproject.com/pt-br/2.1/ref/contrib/auth/

    # atributos adicionais (personalizados)
    portfolio_site = models.URLField(blank=True) # optional, can be blank

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # optional

    def __str__(self):
        return self.user.username
