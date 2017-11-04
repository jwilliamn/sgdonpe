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
    @staticmethod
    def getLastState(document):
        allStepHistories = StepHistory.objects.filter(document=document)
        if len(allStepHistories) > 0:
            return max(allStepHistories, key=lambda item: item.whenTime).currentPrincipalStateID
        else:
            allStatesWhereDE = PrincipalStates.objects.filter(estado=PrincipalStates.Desconocido)
            if(len(allStatesWhereDE)>0):
                return allStatesWhereDE[0]
            print('no hay ningun estado con Desconocido???')
            return None
    def __str__(self):
        return dict(PrincipalStates.PossibleStates)[self.estado]
    #def __str__(self):

     #   return str(self.estado)


class StepHistory(models.Model):
    document = models.ForeignKey(Document)
    currentPrincipalStateID = models.ForeignKey(PrincipalStates)
    externUserID = models.IntegerField(null=True)
    user = models.ForeignKey(User)
    whenTime = models.DateTimeField(auto_now=True)
    previousStepHistory = models.ForeignKey('self', null=True)
    comentario = models.CharField(max_length=200,default='Sin comentario')
    @staticmethod
    def getAllHistory(idDocument):
        allHistory = StepHistory.objects.filter(document=idDocument)
        toReturn = {}
        toReturn['totalLog'] = len(allHistory)
        for indx in range(len(allHistory)):
            dic = {}
            dic['FechaHora'] = allHistory[indx].whenTime
            dic['UsuarioExterno'] = allHistory[indx].externUserID
            dic['Comentario'] = allHistory[indx].comentario
            dic['estado'] = str(allHistory[indx].currentPrincipalStateID)
            dic['Usuario'] = allHistory[indx].user.username
            dic['Email'] = allHistory[indx].user.email

            toReturn['Log' + str(indx)] = dic
        return JsonResponse(toReturn)

    @staticmethod
    def getLastState(document):
        return PrincipalStates.getLastState(document)