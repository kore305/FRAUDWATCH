from django.urls import path
from .views import report_scam_view

urlpatterns = [
    path('report/', report_scam_view, name='report_scam'),
]
