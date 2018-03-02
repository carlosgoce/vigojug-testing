from django.test import TestCase

from store.models import Author


class AuthorTestCase(TestCase):
    def test_fullname_is_correctly_displayed(self):
        author = Author.objects.create(first_name='Kent', last_name='Beck')
        self.assertEqual('Kent Beck', author.fullname)
