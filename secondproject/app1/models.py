from django.db import models

# Create your models here.
class Training_Candidates(models.Model):
    name = models.CharField(max_lenght = 20)
    contact = models.IntegerField()

    def __str__(self):
        return self.name