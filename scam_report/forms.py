from django import forms
from .models import ScamReport


from django import forms
from .models import ScamReport

class ScamReportForm(forms.ModelForm):
    class Meta:
        model = ScamReport
        fields = ['scam_type', 'description', 'email', 'attachment']
        widgets = {
            'scam_type': forms.Select(attrs={'class': 'w-full py-2 px-4 border rounded'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-2 px-4 border rounded', 'rows': 5}),
            'email': forms.EmailInput(attrs={'class': 'w-full py-2 px-4 border rounded'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-4 border rounded'}),
        }
