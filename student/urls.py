from django.contrib import admin
from django.urls import path
from student.views import (
    fetch_student,
    list_class,
    create_class,
    edit_class,
    delete_class,
    class_students,
    create_student,
    edit_student,
    delete_student,
    StudentView,
    
    
)

urlpatterns = [
    path('fetch/', fetch_student, name='fetch_student'),
    path('view/', StudentView.as_view(), name='view_student'),
    path('class/',list_class, name='list_class'),  
    path('class/create',create_class,name="create_class"),
    path('class/edit/<id>',edit_class,name="edit_class"),
    path('class/students/<id>/', class_students, name='class_students'),
    path('class/delete/<id>',delete_class,name="delete_class"),
    path('create/',create_student,name="create_student"),
    path('edit/<id>',edit_student,name="edit_student"),
    path('delete/<id>',delete_student,name="delete_student"),
 
]