from django.urls import path
from . import views

urlpatterns = [
    path('', views.Task.as_view(), name='tasks'),
    path('<id>', views.TaskDetails.as_view(), name='tasks'),
]
