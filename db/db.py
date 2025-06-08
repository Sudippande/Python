from django.db import models
#student table is created and name.age are column
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
Student.objects.create(name='sudip',age=23)

#get all student
students=Student.objects.all()
#this is just example.
