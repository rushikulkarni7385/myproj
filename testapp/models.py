from django.db import models


# Create your models here.

class Hyd_Jobs(models.Model):
    Company_Name = models.CharField(max_length=64)
    Job_Title = models.CharField(max_length=64)
    Experience = models.CharField(max_length=64)
    Location = models.CharField(max_length=64)
    Salary = models.IntegerField()
    Posted_date = models.CharField(max_length=64)
    Qualification=models.CharField(max_length=32)


class Banglore_Jobs(models.Model):
    Company_Name = models.CharField(max_length=64)
    Job_Title = models.CharField(max_length=64)
    Experience = models.CharField(max_length=64)
    Location = models.CharField(max_length=64)
    Salary = models.IntegerField()
    Posted_date = models.CharField(max_length=64)
    Qualification = models.CharField(max_length=32)


class Pune_Jobs(models.Model):
    Company_Name = models.CharField(max_length=64)
    Job_Title = models.CharField(max_length=64)
    Experience = models.CharField(max_length=64)
    Location = models.CharField(max_length=64)
    Salary = models.IntegerField()
    Posted_date=models.CharField(max_length=64)
    Qualification = models.CharField(max_length=32)

class Chennai_Jobs(models.Model):
    Company_Name = models.CharField(max_length=64)
    Job_Title = models.CharField(max_length=64)
    Experience = models.CharField(max_length=64)
    Location = models.CharField(max_length=64)
    Salary = models.IntegerField()
    Posted_date = models.CharField(max_length=64)
    Qualification = models.CharField(max_length=32)