from django.contrib import admin
from .models import tbl_task, tbl_task_user_assoc

# Register your models here.
admin.site.register(tbl_task)
admin.site.register(tbl_task_user_assoc)