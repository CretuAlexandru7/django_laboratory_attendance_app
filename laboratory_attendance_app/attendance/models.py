from django.db import models
from accounts.models import Student


class Attendance(models.Model):
	class Meta:
		ordering = ['-start_date']

	STATUS = (
		('Upcoming', 'Upcoming'),
		('Done', 'Done')
	)

	students = models.ManyToManyField(Student, null=True)
	lecture_title = models.CharField(primary_key=True, max_length=50)
	short_description = models.CharField(max_length=500, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return self.lecture_title

