#hashroot_project/loan_app/forms.py
from django import forms
from .models import ReverseMortgage

class ReverseMortgageForm(forms.ModelForm):
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