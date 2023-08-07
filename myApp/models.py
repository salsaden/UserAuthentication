from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname + '  ' + self.lastname
class Course(models.Model):
    coursename = models.CharField(max_length=100)
    coursecode =models.CharField(max_length=100)
    duration = models.IntegerField()
    intake = models.CharField(max_length=200,)
    studymode = models.CharField(max_length=200)

    def __str__(self):
        return self.coursecode + '  ' + self.coursename + '  ' + self.intake + '  ' + self.studymode
