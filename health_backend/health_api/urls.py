from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register_user,patient_list_create, patient_detail , doctor_list_create , doctor_detail,patient_doctor_mapping_list, patient_doctor_mappings_by_patient, delete_patient_doctor_mapping
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/auth/register/', register_user, name='register_user'),
    path('api/auth/login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/patients/', patient_list_create, name='patient-list-create'),
    path('api/patients/<int:id>/', patient_detail, name='patient-detail'),
    path('api/doctors/',doctor_list_create , name = 'doctor-list-create' ),
    path('api/doctors/<int:id>/' ,doctor_detail , name = 'doctor-detail'),
    path('api/mappings/', patient_doctor_mapping_list, name='patient-doctor-mapping-list'),  # GET all mappings, POST new mapping
    path('api/mappings/<int:patient_id>/', patient_doctor_mappings_by_patient, name='patient-doctor-mappings-by-patient'),  # GET mappings by patient
    path('api/mappings/delete/<int:id>/', delete_patient_doctor_mapping, name='delete-patient-doctor-mapping'),  # DELETE mapping

]
