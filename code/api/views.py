from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient
from .permissions import IsDoctor
from .serializers import PatientSerializer, CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom view for obtaining JWT tokens (login endpoint)."""
    serializer_class = CustomTokenObtainPairSerializer


class PatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsDoctor]

    def get_queryset(self):
        return Patient.objects.all()