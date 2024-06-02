from django.urls import path
from . views import *






urlpatterns = [

  
    path('', TaskList.as_view(), name= 'index'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('create', CreateTask.as_view(), name='create'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
]