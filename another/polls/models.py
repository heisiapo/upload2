from django.db import models

class File(models.Model):
    fileName = models.CharField(max_length=20)
    file = models.FileField(upload_to='documents', max_length=100, blank=True)
    time = models.DateTimeField(auto_now_add=True)
