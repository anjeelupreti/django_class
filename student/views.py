from django.shortcuts import render, redirect, get_object_or_404
from student.models import BroadwayStudent, BroadwayClass
from django.http import HttpResponse
from student.forms import BroadwayClassForm, BroadwayStudentForm

# Create your views here.
# function based views

def fetch_student(request):
    a = BroadwayStudent.objects.all()
    context = {"data": a}
    return render(request, "student/index.html", context)

def list_student(request):
    return HttpResponse("this is another view for testing")

def list_class(request):
    context = {"data": BroadwayClass.objects.all()}
    return render(request, "class/index.html", context)

def create_class(request):
    form = BroadwayClassForm()
    if request.method == 'POST':
        form = BroadwayClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/class')
        else:
            print(form.errors)

    context = {"data": "this is create class form", "form": form}
    return render(request, "class/create.html", context)

def edit_class(request, id):
    class_data = get_object_or_404(BroadwayClass, id=id)

    if request.method == 'POST':
        form = BroadwayClassForm(request.POST, request.FILES or None, instance=class_data)
        if form.is_valid():
            form.save()
            return redirect('/student/class')
        else:
            print(form.errors)
    else:
        form = BroadwayClassForm(instance=class_data)

    context = {
        "data": class_data,
        "form": form
    }
    return render(request, 'class/edit.html', context) 

def delete_class(request, id):
    BroadwayClass.objects.get(id=id).delete()
    return redirect('/student/class')

# for student 
def create_student(request):
    form = BroadwayStudentForm()
    if request.method == 'POST':
        form = BroadwayStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/fetch')
        else:
            print(form.errors)

    context = {"data": "this is a form to add student", "form": form}
    return render(request, "student/create.html", context)

def edit_student(request, id):
    student_data = get_object_or_404(BroadwayStudent, id=id)

    if request.method == 'POST':
        form = BroadwayStudentForm(request.POST, request.FILES or None, instance=student_data)
        if form.is_valid():
            form.save()
            return redirect('/student/fetch')
        else:
            print(form.errors)
    else:
        form = BroadwayStudentForm(instance=student_data)

    context = {
        "data": student_data,
        "form": form
    }
    return render(request, 'student/edit.html', context) 

def delete_student(request, id):
    BroadwayStudent.objects.get(id=id).delete()
    return redirect('/student/fetch')
