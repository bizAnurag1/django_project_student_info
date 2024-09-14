from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def homepage(request):
    return render (request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contactus.html')

class StudentListView(ListView):
    model = Student
    context_object_name = "all_students"  # default = 'blog_list' (modelname_list)
    template_name = 'student.html'

# class SemesterListView(ListView):
#     model = Semester
#     context_object_name = "sem"  # default = 'blog_list' (modelname_list)
#     template_name = 'student.html'

def student_sem(request, id):
    student_details = Student.objects.get(pk=id)
    student_semester = Semester.objects.filter(student_id = id)
    context = {"student_details":student_details, "student_semester":student_semester}
    return render (request, 'detailed_info.html', context)

def sem_details(request, id):
    semester_details = Semester.objects.get(pk=id)
    context = {"sem_details":semester_details}
    return render (request, 'detailed_sem.html', context)

# class SemesterDetailedView(DetailView):
#     model = Semester
#     template_name = 'detailed_sem.html'
#     context_object_name = "sem"

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__" #or we can do it like this ['title', 'author', 'blog_text']
    template_name = 'new_student.html'
    success_message = "Student enrolled successfully"
    success_url = reverse_lazy('index')

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    fields = "__all__" #or we can do it like this ['title', 'author', 'blog_text']
    template_name = 'edit_student.html'
    success_message = "Student Info updated successfully"
    success_url = reverse_lazy('index')

class SemesterCreateView(SuccessMessageMixin, CreateView):
    model = Semester
    fields = "__all__" #['title', 'blog_text', 'image'] #or we can do it like this "__all__"
    template_name = 'add_semester.html'
    success_message = "Semester added successfully"
    success_url = reverse_lazy('index')

class SemesterUpdateView(SuccessMessageMixin, UpdateView):
    model = Semester
    fields = "__all__" #or we can do it like this ['title', 'author', 'blog_text']
    template_name = 'edit_marks.html'
    success_message = "Student Info updated successfully"
    success_url = reverse_lazy('index')
