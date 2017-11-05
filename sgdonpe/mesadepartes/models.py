from django.db import models
from rest_framework import serializers
# Create your models here.
class DataTransferBetWeenServers(models.Model):
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    codigoUsuario = models.CharField(max_length=8)
    codDependencia = models.CharField(max_length=8, default='ING')
    dependencia = models.CharField(max_length=256)
    dni = models.CharField(max_length=10)
    title = models.CharField(max_length=256)
    file = models.FileField(upload_to='docFiles/')
    internalUserID = models.CharField(max_length=32)
    sgdUrl = models.CharField(max_length=256)




class DataTransferBetWeenServersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataTransferBetWeenServers
        fields = ('nombres', 'apellidos', 'codigoUsuario', 'codDependencia',
                  'dependencia','dni','title','vinternalUserID','sgdUrl')