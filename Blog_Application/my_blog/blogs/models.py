from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
   

class Profile(models.Model):
    bio = models.TextField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
  
class Course(models.Model):
    name = models.CharField(max_length=100)
   

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)


#Model Inheritance
class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Product(CommonInfo):
    name = models.CharField(max_length=100)