from rest_framework.test import APITestCase
from api.models import CustomUser, Patient
from django.utils import timezone


class CustomUserTests(APITestCase):
    """
    Tests for the CustomUser model.
    """

    def test_custom_user_creation(self):
        """
        Check that a CustomUser is created with the correct username.
        """
        user = CustomUser.objects.create(username='testuser')
        self.assertEqual(user.username, 'testuser')

    def test_custom_user_role_default(self):
        """
        Check that the default role for a CustomUser is 'patient'.
        """
        user = CustomUser.objects.create(username='testuser')
        self.assertEqual(user.role, 'patient')

    def test_custom_user_role_assignment(self):
        """
        Check that a CustomUser can be assigned a specific role, like 'doctor'.
        """
        user = CustomUser.objects.create(username='testuser', role='doctor')
        self.assertEqual(user.role, 'doctor')

    def test_custom_user_str_method(self):
        """
        Check that the string representation of a CustomUser is its username.
        """
        user = CustomUser.objects.create(username='testuser')
        self.assertEqual(str(user), 'testuser')


class PatientTests(APITestCase):
    """
    Tests for the Patient model.
    """

    def test_patient_creation(self):
        """
        Check that a Patient is created with the correct date_of_birth and diagnoses.
        """
        patient = Patient.objects.create(
            date_of_birth='2000-01-01',
            diagnoses={'diagnosis': 'flu'}
        )
        self.assertEqual(patient.date_of_birth, '2000-01-01')
        self.assertEqual(patient.diagnoses, {'diagnosis': 'flu'})

    def test_patient_created_at(self):
        """
        Check that the created_at field is automatically set and is a valid datetime.
        """
        patient = Patient.objects.create(
            date_of_birth='2000-01-01',
            diagnoses={'diagnosis': 'flu'}
        )
        self.assertIsNotNone(patient.created_at)
        self.assertTrue(isinstance(patient.created_at, timezone.datetime))

    def test_patient_str_method(self):
        """
        Check that the string representation of a Patient includes its ID and diagnoses.
        """
        patient = Patient.objects.create(
            date_of_birth='2000-01-01',
            diagnoses={'diagnosis': 'flu'}
        )
        self.assertEqual(str(patient), f'Patient {patient.id} - {patient.diagnoses}')