from django import forms
from student.models import StudentClass
class StudentClassForm(forms.ModelForm):
    class Meta:
        model=StudentClass
        exclude=['created_at']
