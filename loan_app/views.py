#hashroot_project/loan_app/views.py

from django.shortcuts import render
import logging
from .forms import ReverseMortgageForm
from .models import ReverseMortgage
from django.http import HttpResponseServerError


# Get an instance of a logger
logger = logging.getLogger(__name__)

# # Formula to calculate the principal limit
def calculate_principal_limit(age, home_value, margin):
    """
    Calculate the Principal Limit for Reverse Mortgage based on the formula derived.
    :param age: Age of the borrower
    :param home_value: Appraised value of the home
    :param margin: Margin rate
    :return: Principal Limit
    """
    return home_value * (1 - (margin / 100)) * (age / 100)



def home(request):
    principal_limit = None
    try:
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

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return HttpResponseServerError("An error occurred. Please try again later.")
