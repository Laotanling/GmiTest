from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
class age(models.Model):
    name=models.CharField(max_length=20)