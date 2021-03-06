from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InternalUser(models.Model):

    user = models.ForeignKey(User)
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    codigoUsuario = models.CharField(max_length=8)
    codDependencia = models.CharField(max_length=8,default='ING')
    dependencia = models.CharField(max_length=256)
    @staticmethod
    def findInternalUser(targetUser):
        allUsers = InternalUser.objects.filter(user=targetUser)
        if len(allUsers) > 0:
            return allUsers[0]
        else:
            possibleDefaultUser = InternalUser.objects.filter(nombres='desconocido')
            if len(possibleDefaultUser)>0:
                return possibleDefaultUser[0]
            anyUser = targetUser
            toRetUser = InternalUser(user=anyUser,
                                     nombres='no'+str(targetUser.pk)[:7],
                                     apellidos='ap'+str(targetUser.pk)[:7],
                                     codigoUsuario='c'+str(targetUser.pk)[:7],
                                     dependencia='dep'+str(targetUser.pk)[:7])
            toRetUser.save()
            return toRetUser

    def __str__(self):
        return self.nombres+' '+self.apellidos+'_'+self.codigoUsuario+'_'+self.dependencia

    @staticmethod
    def getUserMesaDePartes():
        allUsersMesaDePartes=User.objects.filter(username='mesadepartes')
        if len(allUsersMesaDePartes)>0:
            return allUsersMesaDePartes[0]
        return None

    @staticmethod
    def getInternalUserMesaDePartes():
        return InternalUser.findInternalUser(InternalUser.getUserMesaDePartes())

class ExternalUser(models.Model):


    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    codigoUsuario = models.CharField(max_length=8)
    codDependencia = models.CharField(max_length=8,default='ING')
    dependencia = models.CharField(max_length=256)
    urlUser = models.CharField(max_length=128)
    dni = models.CharField(max_length=12)


    @staticmethod
    def createExternalCitizenUser(nombres,apellidos,dni):
        return ExternalUser(nombres = nombres,
                            apellidos = apellidos,
                            codigoUsuario = nombres[:4]+apellidos[:4],
                            codDependencia = 'sindep',
                            dependencia = 'sindep',
                            urlUser = '',
                            dni =dni)

    def __str__(self):
        return self.nombres+' '+self.apellidos+'_'+self.codigoUsuario+'_'+self.dependencia
