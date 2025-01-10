# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
import requests
from django.http import JsonResponse



# Landing page view
def landing_page_view(request):
    return render(request, 'index.html')

# Sign-up view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to profile page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def profile_view(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        phone_number = request.POST.get('phone_number')
        if link:
            # VirusTotal API call for links
            url = "https://www.virustotal.com/vtapi/v2/url/report"
            params = {
                'apikey': settings.VIRUSTOTAL_API_KEY,
                'resource': link
            }
            try:
                response = requests.get(url, params=params)
                verification_result = response.json()
                
                if verification_result['positives'] == 0:
                    safety_message = "This link appears to be safe."
                else:
                    safety_message = f"Warning: This link is flagged by {verification_result['positives']} sources as unsafe."
                return JsonResponse({
                    'verification_result': verification_result,
                    'safety_message': safety_message
                })
            except Exception as e:
                return JsonResponse({'error_message': f"Error verifying link: {str(e)}"})
        elif phone_number:
            # ipqualityscore API call for phone numbers
            url = f"https://www.ipqualityscore.com/api/json/phone/{settings.IPQUALITYSCORE_API_KEY}/{phone_number}"
            try:
                response = requests.get(url)
                api_result = response.json()
                
                verification_result = {
                    'scan_date': api_result.get('success', False),
                    'positives': 1 if api_result.get('fraud_score', 0) >= 50 else 0,
                    'total': 1,
                    'verbose_msg': api_result.get('message', ''),
                    'fraud_score': api_result.get('fraud_score', 0),
                    'country': api_result.get('country', 'Unknown'),
                    'region': api_result.get('region', 'Unknown'),
                    'city': api_result.get('city', 'Unknown'),
                    'carrier': api_result.get('carrier', 'Unknown'),
                    'line_type': api_result.get('line_type', 'Unknown'),
                    'local_format': api_result.get('local_format', ''),
                    'international_format': api_result.get('international_format', ''),
                    'name': api_result.get('name', 'Not available'),
                    'active': api_result.get('active', False),
                    'do_not_call': api_result.get('do_not_call', False),
                    'spammer': api_result.get('spammer', False),
                    'risky': api_result.get('risky', False),
                }
                
                safety_message = "This phone number appears to be safe."
                if verification_result['fraud_score'] >= 50:
                    safety_message = f"Warning: This phone number has a high fraud score of {verification_result['fraud_score']}."
                if verification_result['spammer']:
                    safety_message += " This number has been identified as a spammer."
                
                return JsonResponse({
                    'verification_result': verification_result,
                    'safety_message': safety_message
                })
            except Exception as e:
                return JsonResponse({'error_message': f"Error verifying phone number: {str(e)}"})
    
    return render(request, 'profile.html')


@login_required
def resources_view(request):
    return render(request, 'resources.html')


# Create your views here.
