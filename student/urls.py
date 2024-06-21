from django.contrib import admin
from django.urls import path
from student.views import (
    fetch_student,
    list_class,
    create_class
    
)

urlpatterns = [
    path('fetch', fetch_student, name='fetch-student'),
    path('class/',list_class, name='list-class'),  
    path('class/create',create_class,name='create_class'),
]

