from django import forms 
from main.models import Student,Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['uid','slug','user']
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['uid','slug','user']