from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponse
from .models import *  # Import the necessary models

def home(request):
    return HttpResponse("Hello World Example of PFSD Program")

def about_agr(request):
    return render(request, 'about_agr.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback_text = request.POST.get('feedback')

        # Save the feedback data to the database
        feedback = Feedback(name=name, email=email, feedback=feedback_text)
        feedback.save()

        # Render success message
        message = "Thank you for your feedback!"
        return render(request, 'feedback.html', {'message': message})

    return render(request, 'feedback.html')

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message', '')
        recipient = request.POST.get('email', 'ganeshbomma25@gmail.com')  # Fallback recipient

        # Save email record to the database
        email_record = EmailRecord(
            subject=subject,
            body=message,
            recipient=recipient
        )
        try:
            # Attempt to send the email
            send_mail(
                subject,
                message,
                'bommaganesh25@gmail.com',  # Replace with sender email
                [recipient],
                fail_silently=False,
            )
            email_record.status = True  # Mark as sent
            messages.success(request, "Email sent successfully!")
        except Exception as e:
            email_record.status = False  # Mark as failed
            messages.error(request, f"Failed to send email: {e}")

        # Save the record regardless of the outcome
        email_record.save()

    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def account(request):
    return render(request, 'account.html')

def first(request):
    return render(request, 'first.html')

def project(request):
     if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('project')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('project')

        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('login')

     return render(request,'project.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user using email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Login the user if authentication is successful
            auth_login(request, user)
            return redirect('first')  # Redirect to the home page or dashboard
        else:
            # If authentication fails, display an error message
            messages.error(request, "Invalid email or password.")
            return render(request, 'first.html')  # Stay on the login page

    return render(request, 'login.html')

def product(request):
    return render(request, 'product.html')

def rating(request):
    return render(request, 'rating.html')

def about_section(request):
    return render(request, 'about_section.html')

def climate(request):
    return render(request, 'climate.html')

def items(request):
    return render(request, 'items.html')
def Fertilizer(request):
    return render(request, 'Fertilizer.html')

def Pesticide(request):
    return render(request, 'Pesticide.html')
def Organic_seeds(request):
    return render(request, 'Organic_seeds.html')
def Urea(request):
    return render(request, 'Urea.html')