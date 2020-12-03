from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=20)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class feedback(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField(max_length=20)
    Feedback = models.TextField(blank=True, null=True)
    Rating = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return self.Name

