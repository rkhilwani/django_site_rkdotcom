# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class ResumeUser(models.Model):
    first_name     = models.CharField(max_length=200)
    last_name      = models.CharField(max_length=200)
    email          = models.CharField(max_length=200)
    date_of_birth  = models.DateField('DOB')
    image_url      = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)


class EducationInformation(models.Model):
    """Object to store education inforamtion"""
    rel_user       = models.ForeignKey(ResumeUser, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=200)
    marks_scored   = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    start_year     = models.DateField()
    end_year       = models.DateField()

class WorkingInformation(models.Model):
    """Object to store work information"""
    rel_user        = models.ForeignKey(ResumeUser, on_delete=models.CASCADE)
    joining_date    = models.DateField()
    company_name    = models.CharField(max_length=200)
    role_in_company = models.CharField(max_length=2000)
    leaving_date    = models.DateField()
    is_current      = models.BooleanField(default=False)