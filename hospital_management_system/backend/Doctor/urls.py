# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add/',views.add_doctor,name='add-doctor'),
#     path('show/<int:pk>/',views.show_doctor,name='show-doctor'),
#     path('list/',views.list_doctors,name='list-doctor'),
#     path('update/<int:pk>/',views.update_doctor,name='update-doctor'),
#     path('delete/<int:pk>/',views.delete_doctor),
#     path('add_appointment/',views.add_appoinment),
#     path('list_appointments/',views.list_appoinments),
#     path('show_appointment/<int:pk>/',views.show_appoinment),
#     path('update_appointment/<int:pk>/',views.update_appoinment),
#     path('delete_appointment/<int:pk>/',views.delete_appoinment),
#     path('add_department/',views.add_department),
#     path('list_departments/',views.list_departments),
#     path('show_department/<int:pk>/',views.show_department),
#     path('update_department/<int:pk>/',views.update_department),
#     path('delete_department/<int:pk>/',views.delete_department),
#     path('add_prescription/',views.add_prescription),
#     path('list_prescriptions/',views.list_prescriptions),
#     path('show_prescriptions/<int:pk>/',views.show_prescription),
#     path('update_prescription/<int:pk>/',views.update_prescription),
#     path('delete_prescription/<int:pk>/',views.delete_prescription),
#     path('shifts/', views.shift_list, name='shift-list'),
#     path('shifts/<int:pk>/', views.shift_detail, name='shift-detail'),
#     path('shift_update/<int:pk>/', views.shift_update, name='shift-update'),
#     path('shifts_delete/<int:pk>/', views.shift_delete, name='shift-delete'),
#     path('patients/', views.patient_list, name='patient-list'),
#     path('patient/<int:pk>/', views.patient_detail, name='patient-detail'),
#     path('patient_update/<int:pk>/', views.patient_update, name='patient-update'),
#     path('patients_delete/<int:pk>/', views.patient_delete, name='patient-delete'),
#     path('medicine-types/', views.medicine_type_list, name='medicinetype-list'),
#     path('medicine-types/<int:pk>/', views.medicine_type_detail, name='medicinetype-detail'),
#     path('medicine-types-update/<int:pk>/', views.medicine_type_update, name='medicinetype-update'),
#     path('medicine-types-delete/<int:pk>/', views.medicine_type_delete, name='medicinetype-delete'),
#     path('medicines/', views.medicine_list, name='medicine-list'),
#     path('medicines/<int:pk>/', views.medicine_detail, name='medicine-detail'),
#     path('medicines-update/<int:pk>/', views.medicine_update, name='medicine-update'),
#     path('medicines-delete/<int:pk>/', views.medicine_delete, name='medicine-delete'),
# ]

# Login/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet, basename='doctor')
router.register(r'patients', views.PatientViewSet, basename='patient')
router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'departments', views.DepartmentViewSet, basename='department')
router.register(r'shifts', views.ShiftViewSet, basename='shift')
router.register(r'medicines', views.MedicineViewSet, basename='medicine')
router.register(r'medicine-types', views.MedicineTypeViewSet, basename='medicinetype')
router.register(r'prescriptions', views.PrescriptionViewSet, basename='prescription')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]