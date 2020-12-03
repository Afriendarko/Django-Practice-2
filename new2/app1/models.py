from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# class CustomUser(AbstractUser):
#     pass
#
# # Create your models here.

class students(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name


class feedback(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    Feedback = models.TextField(blank=True, null=True)
    Session = models.TextField(blank=True, null=True)
    Rating = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return self.Name

