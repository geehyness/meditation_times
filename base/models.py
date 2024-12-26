from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null =True, blank = True)
    title = models.CharField(max_length=200, null=False)
    message = models.TextField(null=False)
    year = models.CharField(max_length=4, null=False)
    week = models.CharField(max_length=2, null=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['week']



class SelectedYear(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)
