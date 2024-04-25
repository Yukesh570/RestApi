from django.urls import path
from . import views

urlpatterns =[
    path('task-list/', views.tasklist , name="task-list"),

    path('task-detail/<str:pk>', views.taskdetail , name="task-detail"),
    path('task-create/', views.taskcreate , name="task-createzzzz "),
    path('task-delete/<str:pk>', views.taskdelete , name="task-delete ")

]