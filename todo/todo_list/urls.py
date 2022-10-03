import imp
from django.urls import path

from .views import ToDoList, ToDoDetails


urlpatterns = [
    path('', ToDoList.as_view()),
    path('<int:pk>/', ToDoDetails.as_view())
]