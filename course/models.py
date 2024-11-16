from django.db import models

# Create your models here.
class Count(models.Model):
    number=models.IntegerField()
    countname=models.CharField(max_length=50)

    def __str__(self):
     return f'{self.number}--{self.countname}'

class WhyUs(models.Model):
    icon=models.CharField(max_length=20)
    heading=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return f'{self.icon}--{self.heading}--{self.description}'

class Feature(models.Model):
    icon=models.CharField(max_length=20)
    heading=models.CharField(max_length=200)

    def __str__(self):
        return f'{self.icon}--{self.heading}'