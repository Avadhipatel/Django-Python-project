from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
# Create your views here.

def add_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addstudent.html', {'form':fm, 'stud':stud})

def update_student(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration( instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')