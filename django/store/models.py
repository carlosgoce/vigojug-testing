from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=255)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

# class Product(models.Model):
#     code = models.CharField(max_length=30, unique=True)
#     name = models.CharField(max_length=255, unique=True)



        # Product.objects.create(code="123", name='Test Driven Development: By Example', year='2002')

        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')
