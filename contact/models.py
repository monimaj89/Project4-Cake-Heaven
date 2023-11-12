from django.db import models

# Create your models here.

class Contact(models.Model):
    # Contact Model
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=False)
    subject = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.email