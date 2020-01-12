from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    
    
class Main(models.Model):
    
    userId=models.CharField(max_length=100)
    timestamp=models.IntegerField()
    #timestamp= models.DateTimeField(auto_now_add=True)
    alt=models.FloatField()
    lng=models.FloatField()
    accSpeedX=models.FloatField()
    accSpeedY=models.FloatField()
    accSpeedZ=models.FloatField()
