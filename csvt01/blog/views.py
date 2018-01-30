#coding:utf-8
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
'''def index(req):
    t=loader.get_template('index1.html')
    c=Context({})
    return HttpResponse(t.render(c))
'''
class Person(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def say(self):
        return "I'm "+self.name

def index(req,parm):
    #user=Person('max',38,'male')
    user={'name':'tom','age':23,'sex':'male'}
    book_list1=['python','java','php','web']
    return render_to_response('index.html',{'title':'my page','book_list':book_list1,'user':user,'id':parm})
