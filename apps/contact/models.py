from django.db import models
from apps.blogs.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"

    def __str__(self):
        return f"{self.name} - {self.subject}"
