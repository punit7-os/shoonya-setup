# import subprocess
# import os
# from django.conf import settings
# from django.shortcuts import render
# from django.utils import timezone
# from django.http import JsonResponse
# import pytz


# def dashboard(request):
#     # Construct the script path
#     script_path = os.path.join(settings.BASE_DIR, 'tentothree', 'scripts', 'hello.py')

#     # Specify the full path to the Python executable
#     # python_executable = r"C:\Users\punit\AppData\Local\Programs\Python\Python311\python.exe"

#     try:
#         # Run the script and capture the output
#         result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
#         output = result.stdout
#     except subprocess.CalledProcessError as e:
#         output = f"Error: {e.stderr}"

#     ist = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
    
#     # Format the timestamp as hhmmss ddmmyyyy
#     timestamp = ist.strftime('%H:%M:%S %d/%m/%Y')
#     context = {
#         'console_output': output,
#         'timestamp': timestamp,
#     }
#     # return render(request, 'dashboard.html', {'console_output': output})
#     return render(request, 'dashboard.html', context)

# # # 
# # # from django.shortcuts import render
# # import pandas as pd

# # def fetchdatadaily(request):
# #     # Example DataFrame
# #     # data = {
# #     #     'Name': ['John', 'Anna', 'Peter', 'Linda'],
# #     #     'Age': [28, 24, 35, 32],
# #     #     'City': ['New York', 'Paris', 'Berlin', 'London']
# #     # }

# #     df = pd.DataFrame(data)

# #     # Convert DataFrame to a list of dictionaries
# #     df_records = df.to_dict(orient='records')

# #     # Pass the data to the template
# #     return render(request, 'index.html', {'df_records': df_records})

# # import datetime

# # def get_script_output(request):
# #     script_path = os.path.join(settings.BASE_DIR, 'myapp', 'scripts', 'your_script.py')

# #     try:
# #         result = subprocess.run(['python3', script_path], capture_output=True, text=True, check=True)
# #         output = result.stdout
# #     except subprocess.CalledProcessError as e:
# #         output = f"Script failed with error: {e.stderr}"

# #     # Add a timestamp to the response to check if it refreshes
# #     timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# #     return JsonResponse({'output': output, 'timestamp': timestamp})
# # from django.http import JsonResponse
# # from django.utils import timezone

# # def tentothree_ajax_view(request):
# #     # Your logic to fetch or generate output and timestamp
# #     output = "Updated script output here"  # Replace this with your actual logic
# #     timestamp = timezone.now().strftime('%Y-%m-%d %H:%M:%S')  # Updated timestamp
    
# #     # Return the data as a JSON response
# #     return JsonResponse({
# #         'output': output,
# #         'timestamp': timestamp
# #     })


# new
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
    
    # Format the timestamp as hhmmss ddmmyyyy
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
            return redirect('home')  # Change 'home' to the name of your homepage URL pattern
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
