from django.db import models

# Create your models here.
class Temperature(models.Model):
    """Model definition for Temperature."""

    date = models.DateTimeField(, auto_now=False, auto_now_add=False)
    temperature = models.FloatField()

    class Meta:
        verbose_name = 'Temperature'
        verbose_name_plural = 'Temperatures'

    def __str__(self):
        return str(self.date)

