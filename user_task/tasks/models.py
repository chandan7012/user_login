from django.db import models
from user.models import tbl_user
    
class tbl_task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task_type = models.CharField(max_length=100)
    
class tbl_task_user_assoc(models.Model):
    task_id = models.ForeignKey(tbl_task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    