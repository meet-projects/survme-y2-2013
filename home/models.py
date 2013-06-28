from django.db import models

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=1024)
    author = models.CharField(max_length=32)
    display = models.CharField(max_length=32)
    public = models.BooleanField()
    
class Answer(models.Model):
    survey = models.ForeignKey('Survey')
    text = models.CharField(max_length=64)
    votes = models.IntegerField()
