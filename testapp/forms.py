from django import forms
from testapp.models import Student

class Add_Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
