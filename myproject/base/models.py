from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user_task_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class CompleteModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    user_task_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class TrashModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=100)
    user_task_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)