import requests

def get_geolocation_by_ip(request):
    ip_client = get_client_ip(request)


def get_client_ip(request):
    forwarder = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarder:
        ip = forwarder.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

