from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student

def liststudents(request):
    students = Student.objects.all()
    context = { 'students': students}
    
    return render(request, 'list_students.html', context)

def student(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Record Saved!")
        
    
    context = {}
    
    context['form']=form
    return render(request, 'student.html', context)


def home(request):
    return render(request, "index.html")

def hello(request):
    return HttpResponse("Hello Wrold!")

def pass_data(request):
    some_data = {
        "key": "value",
        "age": "55",
        
    }
    return render(request, 'pass_data.html', context=some_data)


