import datetime
import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Attendance
from .forms import AttendanceForm
from accounts.models import Student


@login_required(login_url="accounts/login")
def createAttendance(request):
	form = AttendanceForm()
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		form = AttendanceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/overview')

	context = {'form': form}
	return render(request, 'attendance_form.html', context)


@login_required(login_url="accounts/login")
def updateAttendance(request, pk):
	attendance = Attendance.objects.get(lecture_title=pk)
	form = AttendanceForm(instance=attendance)
	if request.method == 'POST':
		print('Printing POST:', request.POST)
		# It saves it as an instance and then is saves it!!!
		# Otherwise - without instance= ... it just creates another one.
		form = AttendanceForm(request.POST, instance=attendance)
		if form.is_valid():
			form.save()
			return redirect('/overview')

	context = {'form': form}
	return render(request, 'attendance_form.html', context)


@login_required(login_url="accounts/login")
def deleteAttendance(request, pk):
	attendance = Attendance.objects.get(lecture_title=pk)
	if request.method == "POST":
		attendance.delete()
		return redirect('/overview')

	context = {'attendance': attendance}
	return render(request, "delete_attendance.html", context)


@csrf_exempt
def add_user_to_attendance(request):
	if request.method == 'POST':
		fp_index = json.loads(request.body)['fp_index']
		student = Student.objects.get(fp_index=int(fp_index))
		current_date = datetime.datetime.now()
		attendance_now = Attendance.objects.filter(Q(start_date__lte=current_date) &
		                                           Q(end_date__gte=current_date)).first()

		if attendance_now:
			attendance_now.students.add(student)

		return HttpResponse(student.fp_index)
