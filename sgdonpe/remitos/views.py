from django.shortcuts import render
import json
from sgdonpe.remitos.models import Remito
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def getJsonResponse(request,idRemito):
    if(request.method == 'GET'):
        response = Remito.getRemitoJsonResponseByID(idRemito)
        return response
    return JsonResponse({})

