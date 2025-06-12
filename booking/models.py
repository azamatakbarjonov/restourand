from django.db import models

class Booking(models.Model):
    Ismingiz = models.CharField(max_length=100)
    Emailngiz = models.EmailField()
    Odam = models.CharField(max_length=100)
    Nomer = models.CharField(max_length=12)
    Habar = models.TextField()

    def __str__(self) -> str:
        return self.Ismingiz





