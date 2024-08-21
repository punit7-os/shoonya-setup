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

    # return render(request, 'dashboard.html', {'console_output': output})
    return render(request, 'dashboard.html', {'console_output': output})


# from django.shortcuts import render
import pandas as pd

def fetchdatadaily(request):
    # Example DataFrame
    # data = {
    #     'Name': ['John', 'Anna', 'Peter', 'Linda'],
    #     'Age': [28, 24, 35, 32],
    #     'City': ['New York', 'Paris', 'Berlin', 'London']
    # }
    df = pd.DataFrame(data)

    # Convert DataFrame to a list of dictionaries
    df_records = df.to_dict(orient='records')

    # Pass the data to the template
    return render(request, 'index.html', {'df_records': df_records})

import datetime
def connected_or_not(request):
   
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return JsonResponse({'timestamp': timestamp})
    # Pass the data to the template
    # return render(request, 'index.html', {'df_records': df_records})

