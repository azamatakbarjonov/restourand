from django.db import models

class Service(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service/')
    dsc = models.TextField()


    def __str__(self):
        return self.full_name
    
    