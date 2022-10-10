from email.errors import HeaderParseError
from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="pon le el Genero")
    
    
    def __str__(self):
        return self.name
    
