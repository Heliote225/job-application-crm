from django.db import models

class Application(models.Model):
    STATUS_CHOICES = [
        ('todo', 'À postuler'),
        ('applied', 'Candidature envoyée'),
        ('interview', 'Entretien/Test'),
        ('waiting', 'En attente de réponse'),
        ('rejected', 'Refus'),
        ('offer', 'Offre reçue'),
    ]

    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    date_applied = models.DateField(null=True, blank=True)
    contact_email = models.EmailField(blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.job_title} - {self.company}"