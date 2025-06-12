from django.db import models

class Homehead(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title
    


class Secbut(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default='fa-utensils')


    def __str__(self):
        return self.title
        