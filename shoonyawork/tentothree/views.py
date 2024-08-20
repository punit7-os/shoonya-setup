import subprocess
import os
from django.conf import settings
from django.shortcuts import render

def dashboard(request):
    # Construct the script path
    script_path = os.path.join(settings.BASE_DIR, 'tentothree', 'scripts', 'hello.py')

    # Specify the full path to the Python executable
    # python_executable = r"C:\Users\punit\AppData\Local\Programs\Python\Python311\python.exe"

    try:
        # Run the script and capture the output
        result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e.stderr}"

    return render(request, 'dashboard.html', {'console_output': output})
