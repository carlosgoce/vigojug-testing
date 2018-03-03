from django.db import models

from store import services


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=255)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


class Seller(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    @property
    def fulladdress(self):
        return f'{self.address} {self.city}'

    def set_location(self):
        if self.lat and self.lng:
            return

        location = services.coordinates_for_address(self.fulladdress)
        self.lat = location['lat']
        self.lng = location['lng']

    def save(self, *args, **kwargs):
        self.set_location()
        super().save(*args, **kwargs)
