from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services.create import create_warning
from .services.longpoll import longpoll
from .services.get import get_warnings_from_server
from .services.update import send_to_all
from django.core import serializers
from django_ratelimit.decorators import ratelimit
import json


@method_decorator(csrf_exempt, name='dispatch')
class CreateView(ListView):
    @method_decorator(ratelimit(key='ip', rate='2/m', method='POST', block=True))
    def post(self, request):
        if "LuaSocket" or "InvilsoTestUAGloryToUkraine" in request.META['HTTP_USER_AGENT']:
            data = json.loads(request.body)
            if create_warning(data):
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'info': 'Warning already is exist in DB.'}, status=501)
        else:
            return JsonResponse({'status': 'error', 'info': 'Warning already is exist in DB.'}, status=501)
            

@method_decorator(csrf_exempt, name='dispatch')
class SendAll(ListView):
    def post(self, request):
        data = json.loads(request.body)
        if send_to_all(data):
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'info': 'Warning already is sended.'}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class LPView(ListView):
    def post(self, request):
        data = json.loads(request.body)
        warning = longpoll(data=data)
        if warning:
            return JsonResponse({'status': 'success', 'data': warning})
        else:
            return JsonResponse({'status': 'error', 'info': 'New warnings is not exist in DB'})
            
@method_decorator(csrf_exempt, name='dispatch')
class GetView(ListView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'status': 'success', 'data': serializers.serialize('json', get_warnings_from_server(data=data))})

        
        
