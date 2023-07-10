from django.db import models
from django.conf import settings

class Plan(models.Model):
    objective = models.TextField(null=True, blank=True)
    executed_by = models.CharField(max_length=200, null=True, blank=True)
    execution_time = models.CharField(max_length=200, null=True, blank=True)
    execution_tracker = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    approved = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['department']


class Activities(models.Model):
    activity = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='activities')
