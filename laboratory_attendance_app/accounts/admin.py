from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	readonly_fields = ('fp_index',)
	list_display = ('fp_index', 'phone', 'grd_average', 'is_teacher')


admin.site.register(Student, StudentAdmin)


