from django.db import models

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)
    author = models.CharField(max_length=32)
    display = models.CharField(max_length=32)
    public = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    
class Answer(models.Model):
    survey = models.ForeignKey('Survey')
    text = models.CharField(max_length=64)
    votes = models.IntegerField()

class Comment(models.Model):
    survey = models.ForeignKey('Survey')
    author = models.CharField(max_length=32)
    text = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
