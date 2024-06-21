from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/', admin.site.urls),
    path('student/', include('student.urls')),
    path('syllabus/', include('syllabus.urls')),
    
]
