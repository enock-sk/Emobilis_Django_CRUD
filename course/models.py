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


class Course(models.Model):
    image=models.ImageField(upload_to='images/')
    category=models.TextField()
    price=models.CharField(max_length=50)
    course_details=models.TextField()
    description=models.TextField()
    trainer_profile=models.ImageField(upload_to='images/')
    trainer_link=models.CharField(max_length=30)
    user_rank=models.IntegerField()
    heart_icon_rank=models.IntegerField()
    def __str__(self):
        return f'{self.trainer_link}'

class Team(models.Model):
    image=models.ImageField(upload_to='images/')
    heading=models.TextField()
    span_heading=models.TextField()
    description=models.TextField()
    twitter_link=models.CharField(max_length=30)
    facebook_link=models.CharField(max_length=30)
    instagram_link=models.CharField(max_length=30)
    linkedin_link=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.heading}'

class FooterLink(models.Model):
    heading=models.TextField()
    link1=models.TextField()
    link2=models.TextField()
    link3=models.TextField()
    link4=models.TextField()
    link5=models.TextField()
    def __str__(self):
        return f'{self.heading}'
class About(models.Model):
    image=models.ImageField(upload_to='images/')
    heading=models.TextField()
    description=models.TextField()
    list1=models.TextField()
    list2=models.TextField()
    list3=models.TextField()
    def __str__(self):
        return f'{self.heading}'