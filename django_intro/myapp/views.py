from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
  return HttpResponse("welcome to django")

def about(request):
    return render(request,'about.html')