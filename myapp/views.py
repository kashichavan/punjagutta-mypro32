from django.shortcuts import render

# Create your views here.

def home(request):
    data={
       'info':[
           ['raja',22,'Hyderabad'],
           ['rani',23,'Tirupati'],
           ['hero',24,'Bengaluru'],
       ]
    }
    return render(request,'home.html',context=data)
