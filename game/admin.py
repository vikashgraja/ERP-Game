from django.contrib import admin
from .models import score
from import_export.admin import ExportActionMixin

# Register your models here.
class scoreAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'attempts', 'start_time', 'H_1', 'H_2', 'H_3', 'H_4', 'end_time', 'time_taken', 'marks')

admin.site.register(score, scoreAdmin)
