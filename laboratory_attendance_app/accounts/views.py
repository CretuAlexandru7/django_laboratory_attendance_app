from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, UpdateView

from .forms import StudentForm, CreateUserForm, UpdateStudentForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from attendance.models import Attendance
from django.contrib import messages
from django.http import HttpResponse
from .models import Student
import json

# GLOBAL VARS:
ACADEMIC_NO_OF_WEEKS = 16


def registerPage(request):
	# If an authenticated user tries to acces the login page:
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				# Make the first name field = username (match th fp_index)
				user_name = form.cleaned_data.get('username')
				new_student = Student.objects.create(
					fp_index=user_name
				)
				new_student.save()
				messages.success(request, 'Account was created for ' + user_name)

				return redirect('login')

		context = {'form': form}
		return render(request, 'accounts/register.html', context)


def loginPage(request):
	# If an authenticated user tries to acces the login page:
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect!')

		context = {}
		return render(request, 'accounts/login.html', context)


def logoutPage(request):
	logout(request)
	return redirect('login')


# General information about the class:
def home(request):
	return render(request, 'accounts/home.html')


@login_required(login_url="login")
# Class dashboard: info / stats
def overview(request):
	students = Student.objects.all()
	attendances = Attendance.objects.all()

	students_no = students.count()
	done_courses = attendances.filter(status='Done').count()
	remaining_courses = ACADEMIC_NO_OF_WEEKS - done_courses

	context = {'students': students, 'attendances': attendances,
	           'students_no': students_no, 'done_courses': done_courses,
	           'remaining_courses': remaining_courses}

	return render(request, 'accounts/overview.html', context)


# General information about the students:
@login_required(login_url="login")
def profile(request, pk):
	context = {}

	if request.user.is_staff and int(pk) == int(request.user.username):
		return redirect('overview')

	student = Student.objects.get(fp_index=pk)
	attendances = Attendance.objects.filter(students=student)
	total_attendances = attendances.count()
	done_attendances = Attendance.objects.filter(status='Done').count()
	b_show_admin_fields = False
	logged_student = Student
	try:
		logged_student = Student.objects.get(user=request.user)
	except Student.DoesNotExist:
		logged_student.fp_index = -1

	if request.user.is_staff or logged_student.fp_index == int(pk):
		b_show_admin_fields = True

	context = {'attendances': attendances, 'student': student,
	           'total_attendances': total_attendances, 'pk': int(pk),
	           'b_show_admin_fields': b_show_admin_fields, 'done_attendances': done_attendances}

	return render(request, 'accounts/profile.html', context)


class UpdateStudent(UpdateView):
	form_class = UpdateStudentForm
	model = Student
	template_name = 'accounts/student_form.html'
	success_url = '/overview'


@login_required(login_url="login")
def deleteStudent(request, pk):
	student = Student.objects.get(fp_index=pk)
	if request.method == "POST":
		student.delete()
		return redirect('/overview')

	context = {'student': student}
	return render(request, "accounts/delete_student.html", context)


"""
- SECTION - Register / create student using a POST command for the NodeMcu requests: 
"""


@csrf_exempt
def create_user(request):
	if request.method == 'POST':
		fp_index = json.loads(request.body)['fp_index']
		new_user = User.objects.create_user(username=fp_index, password="defaultpassword")
		new_student = Student.objects.create(fp_index=fp_index, user=new_user, phone="PHONE", grd_average="1")
		return HttpResponse(new_student.fp_index)

# @login_required(login_url="login")
# def updateStudent(request, pk):
# 	student = Student.objects.get(fp_index=pk)
# 	form = StudentForm(instance=student)
# 	if request.method == 'POST':
# 		print('Printing POST:', request.POST)
# 		# It saves it as an instance and then is saves it!!!
# 		# Otherwise - without instance= ... it just creates another one.
# 		form = StudentForm(request.POST, instance=student)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/overview')
#
# 	context = {'form': form}
# 	return render(request, 'accounts/student_form.html', context)
