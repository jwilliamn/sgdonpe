from django.db import models
from django.contrib.auth.models import User
from sgdonpe.documents.models import Document
from sgdonpe.authentication.models import ExternalUser

# Create your models here.
import json
from django.http import JsonResponse

class PrincipalStates(models.Model):
    ENPROYECTO = 'ENPROYEC'
    PARADESPACHO = 'PARADESP'
    EMITIDO = 'EMITIDO'
    RECIBIDO = 'RECIB'
    RECIBIDOPARCIAL = 'RECIBPAR'
    ATENDIDO = 'ATEND'
    ATENDIDOPARCIAL = 'ATENDPAR'
    ARCHIVADO = 'ARCH'

    PossibleStates = (
        (ENPROYECTO, 'En Proyecto'),
        (PARADESPACHO, 'Para Despacho'),
        (EMITIDO, 'Emitido'),
        (RECIBIDO, 'Recibido'),
        (RECIBIDOPARCIAL, 'Recibido Parcial'),
        (ATENDIDO, 'Atendido'),
        (ATENDIDOPARCIAL, 'Atendido Parcial'),
        (ARCHIVADO, 'Archivado')
    )

    estado = models.CharField(
        max_length=2,
        choices=PossibleStates,
        default=EMITIDO,
    )
    @staticmethod
    def getLastState(document):
        allStepHistories = StepHistory.objects.filter(document=document)
        if len(allStepHistories) > 0:
            return max(allStepHistories, key=lambda item: item.whenTime).currentPrincipalStateID
        else:
            allStatesWhereDE = PrincipalStates.objects.filter(estado=PrincipalStates.ENPROYECTO)
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
    externUserID = models.ForeignKey(ExternalUser,null=True)
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
            dic['UsuarioExterno'] = str(allHistory[indx].externUserID)
            dic['Comentario'] = allHistory[indx].comentario
            dic['estado'] = str(allHistory[indx].currentPrincipalStateID)
            dic['Usuario'] = allHistory[indx].user.username
            dic['Email'] = allHistory[indx].user.email

            toReturn['Log' + str(indx)] = dic
        return JsonResponse(toReturn)

    @staticmethod
    def getLastState(document):
        return PrincipalStates.getLastState(document)