# Django
from django.db import models

class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.username} - {self.created_at}'
