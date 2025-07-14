from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet, basename='doctor')
router.register(r'patients', views.PatientViewSet, basename='patient')
router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'departments', views.DepartmentViewSet, basename='department')
router.register(r'shifts', views.ShiftViewSet, basename='shift')
router.register(r'medicines', views.MedicineViewSet, basename='medicine')
router.register(r'medicine-types', views.MedicineTypeViewSet, basename='medicinetype')
router.register(r'prescriptions', views.PrescriptionViewSet, basename='prescription')

urlpatterns = [
    path('', include(router.urls)),
]
