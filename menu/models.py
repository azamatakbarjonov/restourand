from django.db import models

class Menu(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu/')
    

    def __str__(self):
        return self.full_name
    