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
            ])
        }