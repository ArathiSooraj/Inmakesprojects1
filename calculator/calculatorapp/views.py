from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def calculator(request):
    return render(request,'index.html')

def addition (request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    result1=x+y
    result2=x*y
    result3=x-y
    result4=x/y
    return render(request,"result.html",{'add':result1,'mul':result2,'sub':result3,'div':result4})
