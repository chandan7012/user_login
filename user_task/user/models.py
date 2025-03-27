from django.db import models

# Create your models here.
class tbl_user(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    salt_key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)