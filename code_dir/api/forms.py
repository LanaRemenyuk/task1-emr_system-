from django import forms

from .models import Patient


class PatientAdminForm(forms.ModelForm):
    diagnoses_str = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
        required=False,
        label="Diagnoses (comma separated)",
        help_text="Enter diagnoses as comma separated values.",
    )

    class Meta:
        model = Patient
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.diagnoses:
            self.fields["diagnoses_str"].initial = ", ".join(
                self.instance.diagnoses
            )
        else:
            self.fields["diagnoses_str"].initial = ""

    def clean_diagnoses_str(self):
        """Преобразует строку диагнозов в список."""
        diagnoses_str = self.cleaned_data.get("diagnoses_str", "")
        return (
            [item.strip() for item in diagnoses_str.split(",")]
            if diagnoses_str
            else []
        )

    def save(self, commit=True):
        """Сохраняет список диагнозов."""
        instance = super().save(commit=False)
        diagnoses_list = self.cleaned_data.get("diagnoses_str", [])
        instance.diagnoses = diagnoses_list
        if commit:
            instance.save()
        return instance
