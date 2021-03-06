from django.db import models
import json
from django.http import JsonResponse
# Create your models here.
class Remito(models.Model):
    ADMINISTRATIVO = 'ADMI'
    MESADEPARTES = 'MESA'

    PossibleTipos = (
        (ADMINISTRATIVO, 'Administrativo'),
        (MESADEPARTES, 'Mesa de partes')
    )
    tipo = models.CharField(
        max_length=4,
        choices=PossibleTipos,
        default=MESADEPARTES,
        null=False
    )

    codigo = models.CharField(max_length=32, null=False)

    ENPROYECTO = 'ENPROYEC'
    PARADESPACHO = 'PARADESP'
    EMITIDO = 'EMITIDO'
    RECIBIDO  = 'RECIB'
    RECIBIDOPARCIAL = 'RECIBPAR'
    ATENDIDO = 'ATEND'
    ATENDIDOPARCIAL  = 'ATENDPAR'
    ARCHIVADO = 'ARCH'

    PossibleEstados = (
        (ENPROYECTO , 'En Proyecto'),
        (PARADESPACHO , 'Para Despacho'),
        (EMITIDO ,'Emitido'),
        (RECIBIDO  , 'Recibido'),
        (RECIBIDOPARCIAL , 'Recibido Parcial'),
        (ATENDIDO ,'Atendido'),
        (ATENDIDOPARCIAL  ,'Atendido Parcial'),
        (ARCHIVADO ,'Archivado')
    )
    estado = models.CharField(
        max_length=10,
        choices=PossibleEstados,
        null=False
    )

    codigoDependenciaRemitente = models.CharField(max_length=8, null=True)

    dependenciaRemitente = models.CharField(max_length=256, null=True)

    codigoEncargadoRemitente = models.CharField(max_length=8, null=True)

    encargadoRemitente = models.CharField(max_length=128, null=True)

    ruc = models.CharField(max_length=15, null=True)

    personaJuridica = models.CharField(max_length=128, null=True)

    dni = models.CharField(max_length=8, null=True)

    ciudadano = models.CharField(max_length=128, null=True)

    otroOrigen = models.CharField(max_length=128, null=True)

    codigoOtroOrigen = models.CharField(max_length=128, null=True)

    codigoTipoDoc = models.CharField(max_length=5, null=True)

    descripcionTipoDoc = models.CharField(max_length=32, null=True)

    numeroDoc =  models.CharField(max_length=32, null=True)

    fecha = models.DateTimeField(auto_now=True)

    asunto =  models.CharField(max_length=512, null=True)


    @staticmethod
    def getRemitoJsonResponseByID(idRemito):
        remito = Remito.objects.filter(pk=idRemito)
        if( len(remito) > 0):
            return remito[0].getRemitoJsonResponse()
        return JsonResponse({})


    def getRemitoJsonResponse(self):
        toReturn = {}
        toReturn['tipo'] = self.tipo
        toReturn['codigo'] = self.codigo
        toReturn['estado'] = self.estado
        toReturn['codigoDependenciaRemitente'] = self.codigoDependenciaRemitente
        toReturn['dependenciaRemitente'] = self.dependenciaRemitente
        toReturn['codigoEncargadoRemitente'] = self.codigoEncargadoRemitente
        toReturn['encargadoRemitente'] = self.encargadoRemitente
        toReturn['ruc'] = self.ruc
        toReturn['personaJuridica'] = self.personaJuridica
        toReturn['dni'] = self.dni
        toReturn['ciudadano'] = self.ciudadano
        toReturn['codigoOtroOrigen'] = self.codigoOtroOrigen
        toReturn['otroOrigen'] = self.otroOrigen
        toReturn['codigoTipoDoc'] = self.codigoTipoDoc
        toReturn['descripcionTipoDoc'] = self.descripcionTipoDoc
        toReturn['numeroDoc'] = self.numeroDoc
        toReturn['fecha'] = self.fecha
        toReturn['asunto'] = self.asunto
        #return json.dumps(toReturn, separators=(',', ':'))
        return JsonResponse(toReturn)



class Destino(models.Model):

    codigoDestino = models.CharField(max_length=32, null=False)
    #codigoRemito = models.CharField(max_length=32, null=False)

    codigoRemito = models.ForeignKey(Remito)    
    
    DEPENDENCIA = 'DEPEND'
    PERSONAJURIDICA = 'PERSJU'
    CIUDADANO = 'CIUDA'
    OTROORIGEN = 'OTROOR'

    PossibleTiposDestino = (
        (DEPENDENCIA, 'Dependencia'),
        (PERSONAJURIDICA, 'Persona Juridica'),
        (CIUDADANO, 'Ciudadano'),
        (OTROORIGEN, 'Otro origen')
    )
    tipoDestino = models.CharField(
        max_length=8,
        choices=PossibleTiposDestino,
        default=PERSONAJURIDICA,
        null=False
    )

    NOLEIDODES = 'NOLEIDO'
    RECIBIDODES = 'RECIBIDO'
    ATENDIDODES = 'ATENDIDO'
    ARCHIVADODES = 'ARCHIVADO'

    PossibleEstadosDestino = (
        (NOLEIDODES , 'No leido'),
        (RECIBIDODES  , 'Recibido'),
        (ATENDIDODES ,'Atendido'),
        (ARCHIVADODES ,'Archivado')
    )
    estadoDestino = models.CharField(
        max_length=10,
        choices=PossibleEstadosDestino,
        null=False
    )

    codigoDependenciaDestino = models.CharField(max_length=8, null=True)
    dependenciaDestino = models.CharField(max_length=256, null=True)

    rucDestino = models.CharField(max_length=15, null=True)
    personaJuridicaDestino = models.CharField(max_length=128, null=True)
    dniDestino = models.CharField(max_length=8, null=True)
    ciudadanoDestino = models.CharField(max_length=128, null=True)
    codigoOtroOrigenDestino = models.CharField(max_length=128, null=True)
    otroOrigenDestino = models.CharField(max_length=128, null=True)


    @staticmethod
    def getDestinoJsonResponseByID(idDestino):
        destino = Destino.objects.filter(pk=idDestino)
        if( len(destino) > 0):
            return destino[0].getDestinoJsonResponse()
        return JsonResponse({})


    def getDestinoJsonResponse(self):
        toReturnDes = {}
        toReturnDes['codigoDestino'] = self.codigoDestino
        toReturnDes['codigoRemito'] = self.codigoRemito
        toReturnDes['tipoDestino'] = self.tipoDestino
        toReturnDes['estadoDestino'] = self.estadoDestino
        toReturnDes['codigoDependenciaDestino'] = self.codigoDependenciaDestino
        toReturnDes['dependenciaDestino'] = self.dependenciaDestino
        toReturnDes['rucDestino'] = self.rucDestino
        toReturnDes['personaJuridicaDestino'] = self.personaJuridicaDestino
        toReturnDes['dniDestino'] = self.dniDestino
        toReturnDes['ciudadanoDestino'] = self.ciudadanoDestino
        toReturnDes['codigoOtroOrigenDestino'] = self.codigoOtroOrigenDestino
        toReturnDes['otroOrigenDestino'] = self.otroOrigenDestino
        #return json.dumps(toReturn, separators=(',', ':'))
        return JsonResponse(toReturnDes)


class Referencia(models.Model):
    codigoRef = models.CharField(max_length=32, null=False)
    #codigoDocRemito = models.CharField(max_length=32, null=False)
    codigoDocRemito = models.ForeignKey(Remito)
    codigoDocRemitoRef = models.CharField(max_length=32, null=False)

    @staticmethod
    def getReferenciaJsonResponseByID(idReferencia):
        referencia = Referencia.objects.filter(pk=idReferencia)
        if( len(referencia) > 0):
            return referencia[0].getidReferenciaJsonResponse()
        return JsonResponse({})


    def getidReferenciaJsonResponse(self):
        toReturnRef = {}
        toReturnRef['codigoRef'] = self.codigoRef
        toReturnRef['codigoDocRemito'] = self.codigoDocRemito
        toReturnRef['codigoDocRemitoRef'] = self.codigoDocRemitoRef
        return JsonResponse(toReturnRef)