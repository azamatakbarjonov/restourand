from django.db import models

class Signup(models.Model):
    Full_name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Message = models.TextField()

    is_published = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.Full_name
    