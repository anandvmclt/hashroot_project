#hashroot_project/loan_app/forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import ReverseMortgage

class ReverseMortgageForm(forms.ModelForm):
    age = forms.IntegerField(
        validators=[
            MinValueValidator(50, message='Age must be at least 50 years old.'),
            MaxValueValidator(100, message='Age cannot exceed 100 years old.')
        ],
        widget=forms.NumberInput(attrs={'min': 50, 'max': 100, 'type': 'number'})
    )

    class Meta:
        model = ReverseMortgage
        fields = ['age', 'home_value', 'margin']
        widgets = {
            'margin': forms.Select(choices=[
                (1.0, '1%'),
                (1.5, '1.5%'),
                (2.0, '2%'),
                (2.5, '2.5%'),
                (3.0, '3%'),
                (3.5, '3.5%'),
                (4.0, '4%'),
                (4.5, '4.5%'),
                (5.0, '5%'),
            ])
        }
