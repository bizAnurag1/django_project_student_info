from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contactus"),
    path('students/', views.StudentListView.as_view(), name="index"),
    path('detailed_info/<int:id>', views.student_sem, name="student_sem"),
    path('edit_info/<int:pk>', views.StudentUpdateView.as_view(), name = "edit_info"),
    path('detailed_sem/<int:id>', views.sem_details, name="detailed_sem"),
    path('edit_marks/<int:pk>', views.SemesterUpdateView.as_view(), name = "edit_marks"),
    path('new_student/', views.StudentCreateView.as_view(), name="new_student"),
    path('add_sem/', views.SemesterCreateView.as_view(), name = "add_sem"),
]