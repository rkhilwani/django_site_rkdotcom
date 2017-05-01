# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EducationInformation(models.Model):
    """Object to store education inforamtion"""
    institute_name = models.CharField(max_length=200)
    marks_scored   = models.DecimalField(default=0.0)
    start_year     = models.DateField()
    end_year       = models.DateField()

class WorkingInformation(models.Model);
    """Object to store work information"""
    joining_date   = models.DateField()
    company_name   = models.CharField(max_length=200)