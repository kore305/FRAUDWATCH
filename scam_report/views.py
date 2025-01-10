from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ScamReportForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # Bypass CSRF for the browser extension, but be cautious with this in production
def report_scam_view(request):
    if request.method == 'POST':
        # Handle AJAX requests from the browser extension
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = ScamReportForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": "Scam reported successfully!"})
            else:
                return JsonResponse({"errors": form.errors}, status=400)
        
        # Handle regular form submissions from the web page
        else:
            form = ScamReportForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'scam_report/thank_you.html')
    else:
        form = ScamReportForm()
    
    return render(request, 'scam_report/report_scam.html', {'form': form})
