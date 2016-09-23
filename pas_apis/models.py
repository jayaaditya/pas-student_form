from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

from datetime import date
# Create your models here.


class StudentUser(User):
    RollNo = models.CharField(max_length=10)

class StudentProfile(models.Model):
    """Model that gives that stores the studnt profile. It also has fields inherited from StudentUser"""
    StudUser = models.OneToOneField(StudentUser, on_delete = models.CASCADE, primary_key=True)
    FirstName = models.CharField(max_length=100, blank=True)
    LastName = models.CharField(max_length=100, blank=True)
    MiddleName = models.CharField(max_length=100, blank=True)
    XBoard = models.BooleanField(default=False) #shows whether the profile has X class Board details. All profiles need not have 
    XIIBoard = models.BooleanField(default=False)# show whether the profile has XII class Board details.
    UnderGrad = models.BooleanField(default=False)# shows whether the profile has undergrad details.
    PostGrad = models.BooleanField(default=False)# shows whether the profile has postgrad details.

class XBoard(models.Model):
    Profile = models.OneToOneField(StudentProfile, on_delete = models.CASCADE, primary_key=True)
    Date = models.DateField(blank=True)
    Marks = models.IntegerField()
    Board = models.CharField(max_length=100)
    @classmethod
    def create(cls, Profile):
        XBoard = cls(Profile=Profile)
        undergrad.Profile.XBoard = True
        return XBoard

class XIIBoard(models.Model):
    """Model containing XII Board Details, having OneToOne relation with StudentProfile"""
    Profile = models.OneToOneField(StudentProfile, on_delete = models.CASCADE, primary_key=True)
    Marks = models.IntegerField()
    Board = models.CharField(max_length=100)
    Date = models.DateField(blank=True)

    @classmethod
    def create(cls, Profile):
        XIIBoard = cls(Profile=Profile)
        undergrad.Profile.XIIBoard = True
        return XIIBoard

class StudentUnderGrad(models.Model):
    """Model containing UnderGrad Details, having OneToOne relation with StudentProfile"""
    Profile = models.OneToOneField(StudentProfile, on_delete = models.CASCADE, primary_key=True)
    Cpi = models.FloatField()
    ParentBranch = models.CharField(max_length=100)
    Institute = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    @classmethod
    def create(cls, Profile):
        undergrad = cls(Profile=Profile)
        undergrad.Profile.UnderGrad = True
        return undergrad

class SecondaryMajor(StudentUnderGrad):
    """Model that shows whether the student has opted for a Double Major. Has one-one relation with StudentUnderGrad model """
    SecBranch = models.CharField(max_length=100)

class DualDegree(StudentUnderGrad):
     """Model that shows whether the student has opted for a Double Major. Has one-one relation with StudentUnderGrad model """
     SecBranch = models.CharField(max_length=100)

class StudentPostGrad(models.Model):
    """Model containing PostGrad Details, having OneToOne relation with StudentProfile"""
    Profile = models.OneToOneField(StudentProfile, on_delete = models.CASCADE, primary_key=True)
    Cpi = models.FloatField()
    ParentBranch = models.CharField(max_length=100)
    Institute = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    @classmethod
    def create(cls, Profile):
        postgrad = cls(Profile = Profile)
        postgrad.Profile.PostGrad = True
        return postgrad

class StudentExp(models.Model):
    """Model containing Experience Details, having OneToOne relation with StudentProfile"""
    Profile = models.OneToOneField(StudentProfile, on_delete = models.CASCADE, primary_key=True)
    Intern = models.IntegerField(default=0)
    POR = models.IntegerField(default=0)
    Training = models.IntegerField(default=0)
    Project = models.IntegerField(default=0)

class StudentIntern(models.Model):
    """Model that contains Intern info, related to StudExp and StudentProfile for convinience"""
    Exp = models.ForeignKey(StudentExp)
    Profile = models.ForeignKey(StudentProfile)
    IntProfile = models.CharField(max_length=100)
    Organisation = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Description = models.TextField()

class StudentPOR(models.Model):
    """ Model that contains POR, related to StudExp and StudentProfiloe for convinience"""
    Exp = models.ForeignKey(StudentExp)
    Profile = models.ForeignKey(StudentProfile)
    Position = models.CharField(max_length=100)
    Description = models.TextField()

class StudentTrain(models.Model):
    """Model that contains Training info, related to StudExp and StudentProfile for convinience"""
    Exp = models.ForeignKey(StudentExp)
    Profile = models.ForeignKey(StudentProfile)
    Program = models.CharField(max_length=100)
    Organisation = models.CharField(max_length=100)
    Description = models.TextField()

class StudentProj(models.Model):
    """Model that contains Training info, related to StudExp and StudentProfile for convinience"""
    Exp = models.ForeignKey(StudentExp)
    Profile = models.ForeignKey(StudentProfile)
    StartDate = models.DateField(blank = True)
    EndDate =  models.DateField(blank = True)
    Description = models.TextField()
    ProjectLink = models.TextField(blank = True)
