from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages
from .models import AttendanceSession
from admin_panel.models import Employee  # Make sure this import is correct

def attendance_view(request):
    user = request.user

    employee = Employee.objects.filter(user=user).first()
    if not employee:
        # You can also render a custom template instead of redirect
        messages.error(request, "Only employees can access the attendance system.")
        return redirect('dashboard')  # Or any fallback page

    current_session = AttendanceSession.objects.filter(user=user, check_out__isnull=True).first()
    sessions = AttendanceSession.objects.filter(user=user).order_by('-check_in')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'start':
            if current_session:
                return JsonResponse({'status': 'error', 'message': 'You already have an active session.'})
            session = AttendanceSession.objects.create(user=user)
            return JsonResponse({
                'status': 'success',
                'action': 'start',
                'session_id': session.id,
                'check_in': session.check_in.isoformat()
            })

        elif action == 'stop':
            if not current_session:
                return JsonResponse({'status': 'error', 'message': 'No active session to stop.'})
            current_session.check_out = timezone.now()
            if current_session.is_on_break:
                # End any active break
                current_session.total_break_time += timezone.now() - current_session.break_start
                current_session.break_start = None
                current_session.is_on_break = False
            current_session.save()
            return JsonResponse({
                'status': 'success',
                'action': 'stop',
                'session_id': current_session.id,
                'check_out': current_session.check_out.isoformat(),
                'total_break_time': str(current_session.total_break_time),
            })

        elif action == 'start_break':
            if current_session and not current_session.is_on_break:
                current_session.is_on_break = True
                current_session.break_start = timezone.now()
                current_session.save()
                return JsonResponse({'status': 'success', 'on_break': True})

        elif action == 'end_break':
            if current_session and current_session.is_on_break:
                current_session.total_break_time += timezone.now() - current_session.break_start
                current_session.break_start = None
                current_session.is_on_break = False
                current_session.save()
                return JsonResponse({'status': 'success', 'on_break': False})

        return JsonResponse({'status': 'error', 'message': 'Invalid action'})

    # ✅ Step 3: Render attendance page
    return render(request, 'attendance/attendance.html', {
        'current_session': current_session,
        'sessions': sessions
    })
