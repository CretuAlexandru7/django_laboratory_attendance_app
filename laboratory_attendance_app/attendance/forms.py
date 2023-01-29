from django.forms import ModelForm
from .models import Attendance
from django import forms

from accounts.models import Student


# class AttendanceForm(ModelForm):
# 	class Meta:
# 		model = Attendance
# 		fields = '__all__'

class AttendanceForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Attendance
        fields = ['lecture_title', 'short_description', 'status', 'start_date', 'end_date', 'students']

