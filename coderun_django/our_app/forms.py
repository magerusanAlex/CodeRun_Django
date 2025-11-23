from django import forms
from .models import Instruction

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = '__all__'
        # You can add widgets here to style the inputs with CSS classes if you want