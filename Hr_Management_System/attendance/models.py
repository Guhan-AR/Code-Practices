from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class AttendanceSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(null=True, blank=True)
    is_on_break = models.BooleanField(default=False)
    break_start = models.DateTimeField(null=True, blank=True)
    total_break_time = models.DurationField(default=timedelta)
    def duration(self):
        if self.check_out:
            total_time = self.check_out - self.check_in
            # Convert to total seconds, round, then convert back to timedelta
            total_seconds = (total_time - self.total_break_time).total_seconds()
            return timedelta(seconds=round(total_seconds))
        return None

    def __str__(self):
        return f"{self.user.username} | {self.check_in.strftime('%Y-%m-%d %H:%M')}"
