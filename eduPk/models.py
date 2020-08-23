from django.db import models

# Create your models here.
class University (models.Model):

    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Program (models.Model):

    title = models.CharField(max_length=300)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    fee = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title