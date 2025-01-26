from api.models import CustomUser, Patient
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class CustomTokenObtainPairViewTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="doctor", password="password", role="doctor"
        )
        self.url = reverse("login")

    def test_token_obtain_pair(self):
        """
        Check that a valid user can get JWT access and refresh tokens.
        """
        response = self.client.post(
            self.url,
            {"username": "doctor", "password": "password"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)


class PatientListViewTest(APITestCase):
    def setUp(self):
        self.doctor_user = CustomUser.objects.create_user(
            username="doctor", password="password", role="doctor"
        )
        self.client = APIClient()
        refresh = RefreshToken.for_user(self.doctor_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )

        self.patient1 = Patient.objects.create(
            date_of_birth="2000-01-01", diagnoses={"diagnosis": "flu"}
        )
        self.patient2 = Patient.objects.create(
            date_of_birth="1990-05-15", diagnoses={"diagnosis": "cold"}
        )
        self.url = reverse("patients")

    def test_patient_list_view_doctor_access(self):
        """
        Check that a doctor can access the patient list.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.data[0]["diagnoses"], self.patient1.diagnoses
        )
        self.assertEqual(
            response.data[1]["diagnoses"], self.patient2.diagnoses
        )

    def test_patient_list_view_unauthenticated(self):
        """
        Check that an unauthenticated user cannot access the patient list.
        """
        self.client.credentials()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patient_list_view_patient_access(self):
        """
        Check that a patient cannot access the patient list.
        """
        patient_user = CustomUser.objects.create_user(
            username="patient", password="password", role="patient"
        )
        refresh = RefreshToken.for_user(patient_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patient_list_view_admin_access(self):
        """
        Check that an admin can access the patient list.
        """
        admin_user = CustomUser.objects.create_user(
            username="admin", password="password", role="admin"
        )
        refresh = RefreshToken.for_user(admin_user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
