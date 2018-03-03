import googlemaps

from django.conf import settings


def coordinates_for_address(address):
    gmaps = googlemaps.Client(key=settings.GMAPS_API_KEY)
    result = gmaps.geocode(address)

    if not result:
        return None

    return result[0]['geometry']['location']
