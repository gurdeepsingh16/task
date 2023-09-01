from django.db import models

# Create your models here.

class Contact_us(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    about_yourself = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name
