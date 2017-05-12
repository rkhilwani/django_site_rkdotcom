# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ResumeUser, EducationInformation

# Register your models here.

admin.site.register(ResumeUser)
admin.site.register(EducationInformation)