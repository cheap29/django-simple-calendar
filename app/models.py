import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Schedule(models.Model):
    """スケジュール"""
    summary = models.CharField('user', max_length=50)
    description = models.TextField('schedule', blank=True)
    start_time = models.TimeField('start', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('end', default=datetime.time(7, 0, 0))
    date = models.DateField('date')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.summary

class Memo(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title