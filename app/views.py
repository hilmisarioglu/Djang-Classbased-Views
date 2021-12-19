from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.

def home(request):
    return render(request, "app/home.html")


def student_list(request):

    students = Student.objects.all()

    context = {
        "students":students
    }

    return render(request, "app/student_list.html", context)

def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")


    context = {

       "form":form
    }

    return render(request, "app/student_add.html", context)

def student_detail(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }

    return render(request, "app/student_detail.html", context)

def student_update(request, id):

    student = Student.objects.get(id=id)

    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")

    context= {

        "student":student,
        "form":form
    }

    return render(request, "app/student_update.html", context)

def student_delete(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":


        student.delete()
        return redirect("list")

    context= {
        "student":student
    }
    return render(request, "app/student_delete.html",context)

