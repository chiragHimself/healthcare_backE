from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import register_user,patient_list_create, patient_detail
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('api/auth/register/', register_user, name='register_user'),
    path('api/auth/login/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/patients/', patient_list_create, name='patient-list-create'),
    path('api/patients/<int:id>/', patient_detail, name='patient-detail'),
]
