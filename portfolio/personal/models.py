from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    bio = models.TextField()

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    details = models.TextField()

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField()
    
class Achievement(models.Model):
    description = models.TextField()
    
class Activity(models.Model):
    description = models.TextField()

class Referee(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

