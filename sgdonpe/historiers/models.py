from django.db import models
from django.contrib.auth.models import User
from sgdonpe.documents.models import Document
# Create your models here.
import json
from django.http import JsonResponse

class PrincipalStates(models.Model):
    Desconocido = 'DE'
    Recibido = 'RE'
    Leido = 'LE'
    Visado = 'VI'
    Firmado = 'FI'
    Enviado = 'EN'

    PossibleStates = (
        (Desconocido, 'Desconocido'),
        (Recibido, 'Recibido'),
        (Leido, 'Leido'),
        (Visado, 'Visado'),
        (Firmado, 'Firmado'),
        (Enviado, 'Enviado')
    )
    estado = models.CharField(
        max_length=2,
        choices=PossibleStates,
        default=Desconocido,
    )


class StepHistory(models.Model):
    document = models.ForeignKey(Document)
    currentPrincipalStateID = models.ForeignKey(PrincipalStates)
    externUserID = models.IntegerField(null=True)
    user = models.ForeignKey(User)
    when = models.DateField(auto_now_add=True)
    previousStepHistory = models.ForeignKey('self', null=True)
    comentario = models.CharField(max_length=200,default='Sin comentario')
    @staticmethod
    def getAllHistory(idDocument):

        allHistory = StepHistory.objects.filter(document=idDocument)
        toReturn = {}
        toReturn['totalData'] = len(allHistory)
        return JsonResponse(toReturn)

    @staticmethod
    def get_last_principalState(idDocument):
        allHistory = StepHistory.objects.filter(document=idDocument)
        if len(allHistory)>0:
            return max(allHistory, key=lambda item: item.when).currentPrincipalStateID
        else:
            return None