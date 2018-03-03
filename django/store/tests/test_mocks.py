import pytest

from unittest.mock import patch

from store.models import Seller


@patch('store.models.services.coordinates_for_address',
    lambda x: {'lat': 12345, 'lng': 54321})
@pytest.mark.django_db
def test_set_location_when_location_is_empty():
    seller = Seller(name='Carlos', address='Rúa Roupeiro', city='Vigo')
    seller.save()

    assert seller.lat == 12345
    assert seller.lng == 54321


# TODO
# Añadir otro test the location ya definida
# Hacer otro más de python parametrize
