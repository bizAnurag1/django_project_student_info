from django.contrib import admin
from .models import Student, Semester

# Inline for Semester (to be used in StudentAdmin)
class SemesterInline(admin.TabularInline):
    model = Semester
    extra = 1

# Admin for Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'student_class']
    search_fields = ['name', 'roll_no']
    list_filter = ['student_class']
    inlines = [SemesterInline]  # Inline for Semesters under Student

# Admin for Semester
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['student', 'semester_number', 'maths', 'science', 'history', 'english']

# Register the models in the admin interface
admin.site.register(Student, StudentAdmin)
admin.site.register(Semester, SemesterAdmin)
