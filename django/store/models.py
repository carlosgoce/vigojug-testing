from django.db import models
from django.contrib.auth.models import User

from store import services


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=255)
    subscribers = models.ManyToManyField(User, through='AuthorSubscription')

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)

    def author_subscribers(self):
        return self.author.subscribers.all()

    def publish(self):
        for subscriber in self.author_subscribers():
            subscriber.notify_book_published(self)


class AuthorSubscription(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Seller(models.Model):
    objects = models.Manager()

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
