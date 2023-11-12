from django.db import models

# Create your models here.

class Contact(models.Model):
    # Contact Model
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=False)
    subject = models.CharField(max_length=40, null=False, blank=False)
    message = models.TextField()
    data_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email