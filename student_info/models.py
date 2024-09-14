from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Semester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='semesters')
    semester_number = models.IntegerField(null=True, blank=True) 
    maths = models.IntegerField(null=True, blank=True)
    science = models.IntegerField(null=True, blank=False)
    history = models.IntegerField(null=True, blank=False)
    english = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.semester_number)
    
    # def get_absolute_url(self):
    #     return reverse("detailed_info", kwargs={"pk": self.pk})

