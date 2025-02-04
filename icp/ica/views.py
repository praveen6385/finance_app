from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Borrower

# Define the admin PIN (you can store this in settings.py for better security)
ADMIN_PIN = "1234"  # Replace with your 4-digit PIN

def login(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if pin == ADMIN_PIN:
            # PIN is correct, redirect to home page
            return redirect('home')
        else:
            # PIN is incorrect, show error message
            messages.error(request, "Invalid PIN. Please try again.")
    return render(request, 'ica/login.html')

def home(request):
    # Home page view
    return render(request, 'ica/home.html')

def option1(request):
    if request.method == 'POST':
        # Save form data to the database
        borrower = Borrower(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            loan_amount=float(request.POST.get('loan_amount')),
            loan_tenure=int(request.POST.get('loan_tenure')),
            interest_rate=float(request.POST.get('interest_rate')),
        )
        borrower.save()
        return redirect('option2')  # Redirect to Option 2 after submission
    return render(request, 'ica/option1.html')

def option2(request):
    borrower = Borrower.objects.last()
    context = {'borrower': borrower}
    return render(request, 'ica/option2.html', context)

def option3(request):
    borrowers = Borrower.objects.all()
    context = {'borrowers': borrowers}
    return render(request, 'ica/option3.html', context)

def option4(request):
    return render(request, 'ica/option4.html')

def option5(request):
    return render(request, 'ica/option5.html')