from store import services


def test_coordinates_for_address():
    coordinates = services.coordinates_for_address('Kaleido Coworking')
    assert {'lat': 42.2374301, 'lng': -8.717658} == coordinates
