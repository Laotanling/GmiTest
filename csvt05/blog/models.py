from __future__ import unicode_literals

from django.db import models

# Create your models here.
sex_choices=(
    ('f','famale'),
    ('m','male'),
)
class User(models.Model):
    name=models.CharField(max_length=30)
    sex=models.CharField(max_length=1,choices=sex_choices)
    def __unicode__(self):
        return self.name