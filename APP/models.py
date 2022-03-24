from django.db import models

# Create your models here.

class Kerdes(models.Model):
    kerdes = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Kérdés'
        verbose_name_plural = 'Kérdések'

    def __str__(self):
        """Unicode representation of Kerdes."""
        return f"ez az objektum kérdése: {self.kerdes}"

class SajatUser(models.Model):
    """Model definition for SajatUser."""

    # TODO: Define fields here

    user = models.OneToOneField(User)

    class Meta:
        """Meta definition for SajatUser."""

        verbose_name = 'SajatUser'
        verbose_name_plural = 'SajatUsers'

    def __str__(self):
        """Unicode representation of SajatUser."""
        pass



