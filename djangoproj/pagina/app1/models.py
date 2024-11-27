from django.db import models
class proyect(models.Model):
    name= models.CharField(max_length=200)

class trajes(models.Model):
  title= models.CharField(max_length=150)
  desc= models.TextField()
  project=models.ForeignKey(proyect,on_delete=models.CASCADE)

