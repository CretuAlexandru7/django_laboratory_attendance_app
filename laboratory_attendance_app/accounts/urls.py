from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create_user, name="create_user"),

	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutPage, name="logout"),
	path('register/', views.registerPage, name="register"),
	path('', views.home, name="home"),
	path('profile/<str:pk>', views.profile, name="profile"),
	path('overview/', views.overview, name="overview"),
	#path('update_student/<str:pk>', views.updateStudent, name='update_student'),
	path('update_student/<str:pk>', views.UpdateStudent.as_view(), name='update_student'),
	path('delete_student/<str:pk>', views.deleteStudent, name='delete_student'),
]

