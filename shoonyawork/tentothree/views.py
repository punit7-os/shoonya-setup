
import os
import subprocess
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
import pytz

def dashboard(request):
    # Construct the script path
    script_path = os.path.join(settings.BASE_DIR, 'tentothree', 'scripts', 'hello.py')

    try:
        # Run the script and capture the output
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"

    # Get the current time in Indian Standard Time (IST)
    ist = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
    
    # Format the timestamp as hh:mm:ss dd/mm/yyyy
    timestamp = ist.strftime('%H:%M:%S %d/%m/%Y')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # This is an AJAX request, return JSON response
        return JsonResponse({
            'output': output,
            'timestamp': timestamp
        })

    # If it's a normal request, render the page
    context = {
        'console_output': output,
        'timestamp': timestamp,
        'df_records': [],  # Ensure this is properly populated if used in the template
    }
    return render(request, 'dashboard.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')  # Change 'home' to the name of your homepage URL pattern
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully signed in.')
            return redirect('dashboard')  # Redirect to the homepage or any other page after sign-in
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'join-in.html')