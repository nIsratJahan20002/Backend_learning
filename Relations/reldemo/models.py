from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reldemo_profile')#one to one rel with user
    birth_date = models.DateField(null=True,blank=True)
    bio = models.TextField(max_length=500,blank=True)
    location = models.CharField(max_length=30,blank=True)
    
    def __str__(self):
        return self.user.username

# One-to-Many relationship
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.amount} for {self.category.name}"
    
# Many-to-Many relationship
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    year = models.IntegerField()
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title

# class Profile(models.Model):
#     bio = models.TextField(max_length=500)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.user.username
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.name