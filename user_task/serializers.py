from rest_framework import serializers
from user.models import tbl_user
from tasks.models import tbl_task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_task
        fields = ['title', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbl_user
        fields = ['email', 'password']