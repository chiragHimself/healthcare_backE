from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, UserSerializer , PatientSerializer , DoctorSerializer, PatientDoctorMappingSerializer
from .models import Patient,Doctor, PatientDoctorMapping
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom JWT authentication view using email instead of username"""
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    """API to register a new user"""
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''view handling and utility for patients api'''
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # User must be authenticated
def patient_list_create(request):
    if request.method == 'GET':  
        patients = Patient.objects.filter(user=request.user)  # Only return user's patients
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assign patient to logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def patient_detail(request, id):
    try:
        patient = Patient.objects.get(id=id, user=request.user)  # Ensure user owns patient
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':  # Partial update allowed
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response({"message": "Patient deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

'''view handling and utility for doctors api'''

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])  # User must be authenticated
def doctor_list_create(request):
    if request.method == 'GET':  
        doctors = Doctor.objects.filter(user=request.user)  # Only return user's patients
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Assign patient to logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])  
def doctor_detail(request, id):
    try:
        doctor = Doctor.objects.get(id=id, user=request.user)  # Ensure user owns patient
    except Doctor.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':  # Partial update allowed
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return Response({"message": "Doctor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

''' views for mapping api'''

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def patient_doctor_mapping_list(request):
    if request.method == 'GET':
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def patient_doctor_mappings_by_patient(request, patient_id):
    try:
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_patient_doctor_mapping(request, id):
    try:
        mapping = PatientDoctorMapping.objects.get(id=id)
        mapping.delete()
        return Response({"message": "Mapping deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except PatientDoctorMapping.DoesNotExist:
        return Response({"error": "Mapping not found"}, status=status.HTTP_404_NOT_FOUND)