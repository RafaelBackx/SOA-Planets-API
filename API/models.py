from django.db import models

# Create your models here.

class Planet(models.Model):
    name = models.CharField(max_length=60)
    distance_from_sun = models.IntegerField()
    period_of_revolution = models.IntegerField()
    rotation_speed = models.CharField(max_length=60)
    diameter = models.IntegerField()
    atmosphere_main_components = models.CharField(max_length=100)
    moons = models.IntegerField()
    rings = models.IntegerField()
    def __str__(self):
        return self.name


