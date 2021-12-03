from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100,primary_key=True)
    ans1 = models.CharField(max_length=100,blank=True)
    ans2 = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.username
