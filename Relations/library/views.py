from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def library(request):
    return HttpResponse("hello")
