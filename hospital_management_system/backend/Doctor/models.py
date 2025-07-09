from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=50)
    chief_doctor = models.ForeignKey('Doctor',on_delete=models.SET_NULL,blank=True,null=True,related_name='cheif of the department+')

    def __str__(self):
        return self.name

class Shift(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name}:{self.start_time}-{self.end_time}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.PROTECT,related_name='doctors')
    salary = models.IntegerField()
    shift = models.ForeignKey(Shift,on_delete=models.SET_NULL,null=True,blank=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    experience = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return f"Dr. {self.name}({self.department})"


class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()
    sugar_level = models.IntegerField(null=True,blank=True)
    blood_pressure = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
    ]
    URGENCY_CHOICES = [
        ('ROUTINE', 'Routine'),
        ('URGENT', 'Urgent'),
        ('EMERGENCY', 'Emergency'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')

    scheduled_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='ROUTINE')

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.status} appointment for {self.patient.name} ({self.get_urgency_display()})"


class MediceneType(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=200)
    expiry_date = models.DateField()
    medicene_type = models.ForeignKey(MediceneType,on_delete=models.PROTECT, related_name='medicines')
    warning = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='prescription')
    medicines = models.ManyToManyField(Medicine)
    usage_guidance = models.TextField()

    def __str__(self):
        return f"Prescription for appointment on {self.appointment.scheduled_time.strftime('%Y-%m-%d')}"

