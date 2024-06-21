from django.contrib import admin
from student.models import BroadwayStudent,StudentClass, BroadwayTeacher


# admin.site.register(BroadwayStudent)

# Register your models here.
@admin.register(BroadwayStudent)
class BroadwayStudentAdmin(admin.ModelAdmin):
    list_display=['id','student_class','name','address','phone']
    search_fields=['name','address']
    
@admin.register(BroadwayTeacher)
class StudentTeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','phone','email']
    search_fields=['name','phone''email']

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['id','name','section','teacher',]
    search_fields=['name','section']
    
