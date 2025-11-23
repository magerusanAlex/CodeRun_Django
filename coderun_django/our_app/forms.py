from django import forms
from .models import Instruction


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['direction', 'distance', 'description', 'risk_level', 'previous_instruction']

        # This dictionary controls how the HTML inputs are rendered
        widgets = {
            'direction': forms.Select(attrs={
                'class': 'form-select custom-input',
            }),
            'distance': forms.NumberInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'e.g., 50'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Describe markers, hazards, or landmarks...',
                'rows': 3  # Makes the box shorter and cleaner
            }),
            'risk_level': forms.NumberInput(attrs={
                'class': 'form-control custom-input',
                'placeholder': '0-100',
                'min': 0,
                'max': 100
            }),
            'previous_instruction': forms.Select(attrs={
                'class': 'form-select custom-input',
            })
        }

    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        # Custom label styling (optional, but looks nice)
        self.fields['previous_instruction'].empty_label = "--- Start of Route (No Previous) ---"