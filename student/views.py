from django.shortcuts import render,redirect

from student.models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        student = form.save()
        if "profile_pic" in request.FILES:
            student.profile_pic = request.FILES["profile_pic"]
            student.save()
        return redirect("index")
    context = {
        "form":form
    }
    return render(request,'student/student.html', context)