from django.urls import path

from .views import CustomTokenObtainPairView, PatientListView

urlpatterns = [
    path("login", CustomTokenObtainPairView.as_view(), name="login"),
    path("patients", PatientListView.as_view(), name="patients"),
]
