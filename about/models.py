from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.full_name


class AboutTranslation(models.Model):
    name = models.CharField(_(verbose_name='Enter your name'), max_length=100)
    description = models.CharField(_(verbose_name='Enter your name'), max_length=100)
    message = models.CharField(_(verbose_name='Write your messages'), max_length=100)
    about = models.ForeignKey(to=About, on_delete=models.CASCADE, related_name='about')


class Section(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=50)


    def __str__(self):
        return self.title
    

class Aboutmain(models.Model):
    full_name = models.CharField(max_length=100)
    descrption = models.TextField()
    
    def __str__(self):
        return self.full_name





class Chef(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/')
    twiter = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    
    def __str__(self):
        return self.full_name
        
