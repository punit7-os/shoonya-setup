from django.shortcuts import render
import subprocess
import os
from django.conf import settings

def dashboard(request):
    # Construct the script path using BASE_DIR
    script_path = os.path.join(settings.BASE_DIR, '/tentothree', 'scripts', 'hello.py')

    # Run the script and capture its output
    try:
        result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"

    # Pass the output to the template
    return render(request, 'dashboard.html', {'console_output': output})