from django.conf import settings
from django import http
from account.models import Blocklist

    
class BlockedIpMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
        
    def process_view(self, request, gax, dsa, dac):
        print(request.META['REMOTE_ADDR'], 22)
        if Blocklist.objects.filter(ip=request.META['REMOTE_ADDR']).exists():
            return http.HttpResponseForbidden('{"detail": "Authentication credentials were not provided."}')
        return None