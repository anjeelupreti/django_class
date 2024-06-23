from django import forms
from student.models import BroadwayClass,BroadwayStudent

class BroadwayClassForm(forms.ModelForm):
    # started_date = forms.DateField(widget=forms.DateInput())
    class Meta:
        model = BroadwayClass
        
        exclude =['created_at',]
        # fields = ['name','ended_at']
        
class BroadwayStudentForm(forms.ModelForm):
    class Meta:
        model=BroadwayStudent
        fields ='__all__'