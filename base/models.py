from django.db import models

class Base_main(models.Model):
    maps = models.CharField(max_length=200)
    tel = models.CharField(max_length=15)
    email = models.EmailField()
    online_akk = models.CharField(max_length=150)


    def __str__(self):
        return self.tel
    