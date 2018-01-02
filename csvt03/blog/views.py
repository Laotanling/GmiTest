from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from blog.models import Employee
def index(req):
    emps=Employee.objects.all()
    return render_to_response('index.html',{'emps':emps})