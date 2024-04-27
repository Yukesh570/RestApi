from django.db import models

# Create your models here.
class Task(models.Model):
    # name= models.CharField(max_length=300)
    title= models.CharField(max_length=200,null=True)
    completed = models.BooleanField(default=False, blank=True,null=True)

    # description = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.name


    
    
