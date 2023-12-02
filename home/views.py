import os
from datetime import timezone

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Check if username or email already exists
        if UserDetails.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        if UserDetails.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        if request.POST['Password'] != request.POST['RepeatPassword']:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Proceed with user creation
        user = UserDetails(
            username=request.POST['Username'],
            first_name=request.POST['Firstname'],
            last_name=request.POST['Lastname'],
            email=request.POST['Email'],
            password=make_password(request.POST['Password']),
            is_active=True,
            is_staff=False,
            is_superuser=False,
            last_login=None,
            date_joined=timezone.now()
        )
        user.save()

        return redirect('login')  # Redirect to login after successful registration

    return render(request, 'register.html')


def home(request):
    cookie_value = request.COOKIES.get('toggleState', 'on')
    return render(request, 'home/welcome.html', {'cookie_value': cookie_value})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def cards(request):
    return render(request, 'cards.html')


def charts(request):
    return render(request, 'charts.html')


def resetpwd(request):
    return render(request, 'forgot-password.html')


def tables(request):
    return render(request, 'tables.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def logo(request):
    return render(request, 'logo.html')


# views.py

from django.shortcuts import render
import pandas as pd


def upload_data(request):
    if request.method == 'POST':
        datafile = request.FILES.get('datafile')

        if datafile:
            # Check the file extension
            ext = os.path.splitext(datafile.name)[1]
            if ext.lower() == '.csv':
                df = pd.read_csv(datafile)
            elif ext.lower() in ['.xls', '.xlsx']:
                df = pd.read_excel(datafile, engine='openpyxl')
            else:
                # Handle unsupported file formats
                return render(request, 'error.html', {'message': 'Unsupported file format'})

            # Convert the DataFrame to HTML table
            data_html = df.to_html(classes='table table-bordered')
            context = {'data_table': data_html}
            return render(request, 'tables.html', context)

    return render(request, 'tables.html')

def serve_audio(request, filename):
    file_path = os.path.join('/path/to/audio/', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/mpeg")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

from django.http import HttpResponse

def readCookies(request):
    cookie_value = request.COOKIES.get('toggleState')
    return HttpResponse({cookie_value})
