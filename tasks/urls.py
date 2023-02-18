from django.urls import path
from .views import (
    CreateTasks, ListTasks, UpdateTasks,
    FinishTasks, StartTasks, DeleteTasks
)

app_name = "tasks"

urlpatterns = [
    path('', ListTasks.as_view(), name= 'home_tasks'),
    path('create/', CreateTasks.as_view(), name='create_tasks'),
    path('update/<int:pk>/', UpdateTasks.as_view(), name='update_tasks'),
    path('finish/<int:pk>/', FinishTasks.as_view(), name='finish_tasks'),
    path('start/<int:pk>/', StartTasks.as_view(), name='start_tasks'),
    path('delete/<int:pk>/', DeleteTasks.as_view(), name='delete_tasks'),
]