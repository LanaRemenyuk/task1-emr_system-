from django.test import TestCase
from api.models import Patient
from api.forms import PatientAdminForm


class PatientAdminFormTests(TestCase):
    """
    Tests for the PatientAdminForm.
    """

    def test_form_initialization_with_diagnoses(self):
        """
        Check that the 'diagnoses_str' field is correctly initialized
        when the 'diagnoses' field in the model has data.
        """
        patient = Patient.objects.create(
            date_of_birth='2000-01-01',
            diagnoses=['flu', 'cold']
        )
        form = PatientAdminForm(instance=patient)
        self.assertEqual(form.fields['diagnoses_str'].initial, 'flu, cold')

    def test_form_initialization_without_diagnoses(self):
        """
        Check that the 'diagnoses_str' field is empty
        when the 'diagnoses' field in the model is empty.
        """
        patient = Patient.objects.create(
            date_of_birth='2000-01-01',
            diagnoses=[]
        )
        form = PatientAdminForm(instance=patient)
        self.assertEqual(form.fields['diagnoses_str'].initial, '')

    def test_clean_diagnoses_str(self):
        """
        Check that the 'diagnoses_str' field is correctly cleaned
        and converted into a list of diagnoses.
        """
        form_data = {
            'date_of_birth': '2000-01-01',
            'diagnoses_str': 'flu, cold, fever'
        }
        form = PatientAdminForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['diagnoses_str'], ['flu', 'cold', 'fever'])

    def test_clean_diagnoses_str_empty(self):
        """
        Check that the 'diagnoses_str' field is handled correctly
        when it is empty.
        """
        form_data = {
            'date_of_birth': '2000-01-01',
            'diagnoses_str': ''
        }
        form = PatientAdminForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['diagnoses_str'], [])

    def test_save_with_diagnoses(self):
        """
        Check that the form correctly saves the 'diagnoses' field as a list
        when the 'diagnoses_str' field contains data.
        """
        form_data = {
            'date_of_birth': '2000-01-01',
            'diagnoses_str': 'flu, cold'
        }
        form = PatientAdminForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        patient = form.save()
        self.assertEqual(patient.diagnoses, ['flu', 'cold'])