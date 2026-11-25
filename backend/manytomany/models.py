from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)
    
class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, through='Enrollment')