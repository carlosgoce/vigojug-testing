from unittest.mock import Mock

import pytest

from unittest.mock import patch

from store.models import Book, Seller


# Patching
@patch('store.models.services.coordinates_for_address', lambda x: {'lat': 12345, 'lng': 54321})
@pytest.mark.django_db
def test_set_location_when_location_is_empty():
    seller = Seller(name='Carlos', address='Rúa Roupeiro', city='Vigo')
    seller.set_location()
    assert (12345, 54321) == (seller.lat, seller.lng)


# ⚠
def test_notify_subscribers_when_book_is_published_without_patching():
    subscribers = [Mock(username='User 1'), Mock(username='User 2')]
    book = Book(isbn='0321146530')
    book.author_subscribers = lambda: subscribers

    book.publish()

    subscribers[0].notify_book_published.assert_called_with(book)
    subscribers[1].notify_book_published.assert_called_with(book)


# Mocking
@patch('store.models.Book.author_subscribers')
def test_notify_subscribers_when_book_is_published(author_subscribers):
    '''?'''
    subscribers = [Mock(username='User 1'), Mock(username='User 2')]
    author_subscribers.return_value = subscribers

    book = Book(isbn='0321146530')
    book.publish()

    subscribers[0].notify_book_published.assert_called_with(book)
    subscribers[1].notify_book_published.assert_called_with(book)
