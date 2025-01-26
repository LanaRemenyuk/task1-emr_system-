from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APITestCase, APIRequestFactory
from api.models import CustomUser
from api.permissions import IsAdminOrDoctor


class IsAdminOrDoctorPermissionTests(APITestCase):
    """
    Tests for the IsAdminOrDoctor custom permission.
    """

    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='password', role='admin')
        self.doctor_user = CustomUser.objects.create_user(username='doctor', password='password', role='doctor')
        self.patient_user = CustomUser.objects.create_user(username='patient', password='password', role='patient')

        self.factory = APIRequestFactory()
        self.permission = IsAdminOrDoctor()

    def test_admin_user_has_permission(self):
        """
        Check that an admin user has permission.
        """
        request = self.factory.get('/some-endpoint/')
        request.user = self.admin_user
        has_permission = self.permission.has_permission(request, None)
        self.assertTrue(has_permission)

    def test_doctor_user_has_permission(self):
        """
        Check that a doctor user has permission.
        """
        request = self.factory.get('/some-endpoint/')
        request.user = self.doctor_user
        has_permission = self.permission.has_permission(request, None)
        self.assertTrue(has_permission)

    def test_patient_user_has_no_permission(self):
        """
        Check that a patient user does not have permission.
        """
        request = self.factory.get('/some-endpoint/')
        request.user = self.patient_user
        has_permission = self.permission.has_permission(request, None)
        self.assertFalse(has_permission)

    def test_unauthenticated_user_has_no_permission(self):
        """
        Check that an unauthenticated user does not have permission.
        """
        request = self.factory.get('/some-endpoint/')
        request.user = AnonymousUser()
        has_permission = self.permission.has_permission(request, None)
        self.assertFalse(has_permission)