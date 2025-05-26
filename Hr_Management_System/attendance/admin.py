from django.contrib import admin
from .models import AttendanceSession

@admin.register(AttendanceSession)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'check_in', 'check_out', 'get_work_duration', 'total_break_time')
    list_filter = ('check_in', 'check_out', 'user')

    def get_work_duration(self, obj):
        return obj.duration()
    get_work_duration.short_description = 'Work Duration'
