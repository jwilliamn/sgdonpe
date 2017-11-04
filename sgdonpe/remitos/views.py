from django.shortcuts import render
import json
from sgdonpe.remitos.models import Remito
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from sgdonpe.remitos.models import Destino
from sgdonpe.remitos.models import Referencia


# Create your views here.

def getJsonResponse(request,idRemito):
    if(request.method == 'GET'):
        response = Remito.getRemitoJsonResponseByID(idRemito)
        return response
    return JsonResponse({})


def getJsonResponseDestino(request, idDestino):
	if(request.method == 'GET'):
		response = Destino.getDestinoJsonResponseByID(idDestino)
		return response
	return JsonResponse({})

def getJsonResponseRef(request, idReferencia):
	if(request.method == 'GET'):
		response = Referencia.getReferenciaJsonResponseByID(idReferencia)
		return response
	return JsonResponse({})