from django.urls import path
from . import views

urlpatterns = [
	path('add_user_to_attendance/', views.add_user_to_attendance, name='add_user_to_attendance'),
	path('create_attendance', views.createAttendance, name='create_attendance'),
	path('update_attendance/<str:pk>', views.updateAttendance, name='update_attendance'),
	path('delete_attendance/<str:pk>', views.deleteAttendance, name='delete_attendance'),
]
