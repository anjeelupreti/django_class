from django.shortcuts import render
from student.models import  StudentClass,BroadwayStudent
from django.http import HttpResponse
from student.forms import StudentClassForm

# Create your views here.
# function based views


def fetch_student(request):
    a = BroadwayStudent.objects.all()
    # return HttpResponse(a)
    context = {"data": a}
    return render(request, "student/index.html", context)


def list_class(request):
    context = {"data": StudentClass.objects.filter(status=True)}
    return render(request, "class/index.html", context)

def create_class(request):
    form=StudentClassForm()
    context={'data':'This is create class form','form':form}
    return render(request,'class/create.html',context)
