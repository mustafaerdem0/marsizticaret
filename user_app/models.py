from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    cart = models.ManyToManyField("main_app.Product", verbose_name=("Sepetim"))