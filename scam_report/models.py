from django.db import models

# Create your models here.
class ScamReport(models.Model):
    SCAM_TYPES = [
        ('social_media', 'Social Media Scam'),
        ('phone_call', 'Phone Call Scam'),
        ('website', 'Website Scam'),
        ('email', 'Email Scam'),
        ('other', 'Other Scam')
    ]
    
    scam_type = models.CharField(max_length=50, choices=SCAM_TYPES)
    description = models.TextField()
    email = models.EmailField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scam_type} reported on {self.reported_at}"