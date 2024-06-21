from django.db import models

class BroadwayTeacher(models.Model):
    name = models.CharField(max_length=255, null=True, help_text="Teacher's Name")
    address = models.CharField(max_length=33)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.name}'

class StudentClass(models.Model):
    name = models.CharField(
        verbose_name="Class Name",
        max_length=30,
        blank=True,
        null=True,
    )
    section = models.CharField(
        verbose_name="lab room / section",
        max_length=40
    )
    teacher = models.ForeignKey(BroadwayTeacher, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False)
    class_type = models.CharField(verbose_name="class type", max_length=10, null=True, blank=True)
    class_link = models.URLField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    started_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f'{self.name}:{self.teacher}'
        

class BroadwayStudent(models.Model):
    name = models.CharField(max_length=255, null=True, help_text="student name")
    address = models.CharField(max_length=33)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
