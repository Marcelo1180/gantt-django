from __future__ import unicode_literals

from django.db import models


class Gantt_links(models.Model):
    source = models.IntegerField()
    target = models.IntegerField()
    type = models.CharField(max_length=1)


class Gantt_tasks(models.Model):
    text = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.IntegerField()
    progress = models.FloatField(blank=True, null=True)
    sortorder = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField()

