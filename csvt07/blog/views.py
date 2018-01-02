from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse

# Create your views here.
class UserForm(forms.Form):
    email=forms.CharField()

def register(req):
    if req.method=='POST':
        form=UserForm(req.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse('ok')
    else:
        form=UserForm()
    return  render_to_response('register.html',{'form':form})