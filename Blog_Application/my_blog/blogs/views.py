from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Blog, Book , Author, Student, Course


def index(request):
    
    context ={
         'blogs':Blog.objects.all(),
    }
    return render(request, 'blogs/index.html', context)

def reldemo(request):
    # select_related method use for 1 to M jono.
    books = Book.objects.select_related('author')  # 1 ta qurey, JOIN
    # for book in books:  # normal for loop 
    #     print(book.name, book.author.name)

    # prefetch_related---> M to M
    # students = Student.objects.all()
    # for student in students:
    #     print(student.name,[course.name for course in student.courses.all()])     
    students = models.Student.objects.prefetch_related('courses')  
    for student in students:
         print(student.name,[course.name for course in student.courses.all()])
    return HttpResponse("Hello")




