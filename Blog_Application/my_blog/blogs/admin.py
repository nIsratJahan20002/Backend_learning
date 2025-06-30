from django.contrib import admin
from .models import Blog,Author, Book, Profile, Course, Student

# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Student)