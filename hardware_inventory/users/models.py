from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUser(AbstractUser):
  ROLE_CHOICES = (
    ('ADMIN','Administrator'),
    ('MANAGER','Manager'),
    ('STAFF','Staff'),
  )

  role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='STAFF')

  def __str__(self):
    return self.username
  

  # def generate_token(self):
  #     token, created = Token.objects.get_or_create(user=self)
  #     return token.key