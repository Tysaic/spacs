import requests
import geocoder
from geopy.geocoders import Nominatim 

def get_geolocation_by_ip(request):
    ip_client = get_client_ip(request)


def get_client_ip(request):
    forwarder = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarder:
        ip = forwarder.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def geocoder(location_str):
    #value_to_geocoder = request.query_params['geocoder']
    value_to_geocoder = location_str
    geolocator = Nominatim(user_agent='posters')
    location = geolocator.geocode(value_to_geocoder)
    latitude, longitude = location.latitude, location.longitude
    return {
        "location": location.address,
        "latitude": latitude,
        "longitude": longitude,
    }
