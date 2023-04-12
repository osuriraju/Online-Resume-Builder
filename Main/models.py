from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None,blank=True, null=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.fname


class Education(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None,blank=True, null=True)
    degree1 = models.CharField(max_length=100)
    college1 = models.CharField(max_length=100)
    gpa1 = models.CharField(max_length=10)
    degree2 = models.CharField(max_length=100)
    college2 = models.CharField(max_length=100)
    gpa2 = models.CharField(max_length=10)

    def __str__(self):
        return self.profile.fname
    
class Experience(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,default=None,blank=True, null=True)
    compName1 = models.CharField(max_length=100)
    compPeriod1 = models.CharField(max_length=100)
    compRole1 = models.CharField(max_length=100)
    compName2 = models.CharField(max_length=100)
    compPeriod2 = models.CharField(max_length=100)
    compRole2 = models.CharField(max_length=100)

    def __str__(self):
        return self.profile.fname

class Projects(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,default=None,blank=True, null=True)
    proj1 = models.CharField(max_length=100)
    projDesc1 = models.CharField(max_length=500)
    proj2 = models.CharField(max_length=100)
    projDesc2 = models.CharField(max_length=500)

    def __str__(self):
        return self.profile.fname
    
class Skills(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,default=None,blank=True, null=True)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.profile.fname
    
class Interests(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,default=None,blank=True, null=True)
    interests = models.CharField(max_length=300)

    def __str__(self):
        return self.profile.fname