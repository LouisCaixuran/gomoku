from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse       #导入HttpResponse模块

def index(request):
    return HttpResponse("Hello World!!")

def show_main(request):
    return render(request,'main.html')
