from django.shortcuts import render
from django.http import HttpResponse
from . models import Department
from . models import*
from.forms import BookingForm

# Create your views here.
def index(request):
    # apple={
    #     'name':'student'
    # }
    numbers={
        'num1':10
    }
    # return HttpResponse('Hello World')
    # return render(request, 'index.html',apple)
    return render(request,'index.html',numbers)

def about(request):
    #return HttpResponse('About Page')
    return render(request, 'about.html',)

def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dep={
        'dept':Department.objects.all()
    }
    return render(request,'department.html', dict_dep)

def doctors(request):
    dict_doc={
        'docs':Doctors.objects.all()
    }
    return render(request,'doctors.html', dict_doc)

def booking(request):
    if request.method =='POST':
     form=BookingForm(request.POST)
     if form.is_valid():
        form.save()   
    
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)