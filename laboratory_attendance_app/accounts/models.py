from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fp_index = models.IntegerField(primary_key=True, unique=True)
	phone = models.CharField(max_length=200, null=True)
	grd_average = models.DecimalField(decimal_places=1, max_digits=2, null=True, blank=True)
	is_teacher = models.BooleanField(default=False)

	def __str__(self):
		return self.user.first_name
