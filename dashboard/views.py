'''from django.shortcuts import render
import json
import os

def dashboard_view(request):
    # Assuming your JSON file is in the static directory of your app
    json_file_path = os.path.join('dashboard', 'static', 'jsondata.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    context = {
        'data': data  # Pass the data to the template context
    }

    return render(request, 'dashboard/dashboard.html', context)
'''
from django.shortcuts import render
import json
import os

def calculate_intensity_color(intensity):
    try:
        intensity = int(intensity)
        if intensity <= 5:
            return 'lightgreen'
        elif intensity <= 10:
            return 'green'
        elif intensity <= 15:
            return 'darkgreen'
        else:
            return 'blue'
    except ValueError:
        # Handle the case where intensity is not a valid integer
        return 'white'  # Set a default color or handle it as needed

def dashboard_view(request):
    # Assuming your JSON file is in the static directory of your app
    json_file_path = os.path.join('dashboard', 'static', 'jsondata.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Calculate intensity color for each item
    for item in data:
        item['intensity_color'] = calculate_intensity_color(item['intensity'])

    context = {
        'data': data  # Pass the data to the template context
    }

    return render(request, 'dashboard/dashboard.html', context)
