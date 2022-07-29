from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .services.update import update
from .services.get import get_admins_from_server
from django.core import serializers
import json


@method_decorator(csrf_exempt, name='dispatch')
class UpdateView(ListView):
    def post(self, request, **kwargs):
        kwargs['field']
        data = json.loads(request.body)
        update(data, kwargs['field'])
        return JsonResponse({'status': 'success'})
            
@method_decorator(csrf_exempt, name='dispatch')
class GetView(ListView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'status': 'success', 'data': serializers.serialize('json', get_admins_from_server(data=data))})

        
        
