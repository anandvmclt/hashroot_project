#hashroot_project/loan_app/views.py

from django.shortcuts import render
from .forms import ReverseMortgageForm
from .models import ReverseMortgage

def calculate_principal_limit(age, home_value, margin):
    return home_value * (1 - (margin / 100)) * (age / 100)

def home(request):
    principal_limit = None
    if request.method == 'POST':
        form = ReverseMortgageForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            home_value = form.cleaned_data['home_value']
            margin = form.cleaned_data['margin']
            principal_limit = calculate_principal_limit(age, home_value, margin)

            # Save the calculation result to the database
            reverse_mortgage = ReverseMortgage(
                age=age,
                home_value=home_value,
                margin=margin,
                principal_limit=principal_limit
            )
            reverse_mortgage.save()
    else:
        form = ReverseMortgageForm()

    return render(request, 'loan_app/home.html', {'form': form, 'principal_limit': principal_limit})