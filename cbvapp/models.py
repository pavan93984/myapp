from django.db import models
from django.urls import reverse

# Create your models here.
class school(models.Model):
    school_name = models.CharField(max_length=100)
    principal = models.CharField(max_length=100)
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name
    
    def get_absolute_url(self):
        return reverse ("detail",kwargs={'pk' : self.pk})

class student(models.Model):
    std_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    marks = models.IntegerField()
    grade = models.CharField(max_length=5)
    student = models.ForeignKey(school,related_name='students',on_delete=models.CASCADE)

    def __str__(self):
        return self.std_name   
