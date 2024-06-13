#hashroot_project/loan_app/views.py
from django.shortcuts import render
import logging
from .forms import ReverseMortgageForm
from .models import ReverseMortgage
from django.http import HttpResponseServerError
import json
from .plf_data import plf  # Import PLF data from plf_data.py

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Get sample PLF Value from JSON data
def get_plf(plf_table, age, margin):
    """
    The PLF (Principle loan factor) should be obtain from HUD website
    (https://www.hud.gov/sites/dfiles/SFH/documents/nhm_hecm_101_06_28_21.pdf)
    In the demo we use some sample PLF values from JSON file
    """
    age = str(age)
    margin = str(margin)
    if age in plf_table and margin in plf_table[age]:
        return plf_table[age][margin]
    else:
        raise ValueError("Age or Margin not found in PLF table")


def calculate_principal_limit(plf_table, home_value, age, margin):
    """
    Calculate the Principal Limit for Reverse Mortgage based on the formula derived.
    :param age: Age of the borrower
    :param home_value: Appraised value of the home
    :param margin: Margin rate
    :return: Principal Limit
    :plf - Principle Loan factor from HUD website
    """
    plf = get_plf(plf_table, age, margin)
    principal_limit = home_value * plf
    return principal_limit


# Main functon to manage Django requesta nd response
def home(request):
    principal_limit = None
    try:
        if request.method == 'POST':
            form = ReverseMortgageForm(request.POST)
            if form.is_valid():
                age = form.cleaned_data['age']
                home_value = form.cleaned_data['home_value']
                margin = form.cleaned_data['margin']
                principal_limit = calculate_principal_limit(plf, home_value, age, margin)

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
