from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


job_types = [
    (0, 'tech'),
    (1, 'product'),
    (2, 'operation'),
    (3, 'design')
]


cites = [
    (0, 'Taipei'),
    (1, 'Taichung'),
    (2, 'Kaohsiung')
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=job_types, verbose_name='job_type')
    job_name = models.CharField(max_length=250, blank=False, verbose_name='job_name')
    job_city = models.SmallIntegerField(blank=False, choices=cites, verbose_name='job_city')
    job_responsibility = models.TextField(max_length=1024, verbose_name='job_responsibility')
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name='job_requirement')
    creator = models.ForeignKey(User, verbose_name='creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='created_date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='modify_date', default=datetime.now)
