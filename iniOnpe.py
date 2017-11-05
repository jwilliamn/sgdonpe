from sgdonpe.mesadepartes.models import RegisteredInstitutions
from sgdonpe.authentication.models import InternalUser
from django.contrib.auth.models import User
from sgdonpe.historiers.models import PrincipalStates
from sgdonpe.documents.models import TagModel

ENPROYECTO  = PrincipalStates(estado = 'ENPROYEC')
PARADESPACHO  = PrincipalStates(estado = 'PARADESP')
EMITIDO  = PrincipalStates(estado = 'EMITIDO')
RECIBIDO  = PrincipalStates(estado = 'RECIB')
RECIBIDOPARCIAL  = PrincipalStates(estado = 'RECIBPAR')
ATENDIDO  = PrincipalStates(estado = 'ATEND')
ATENDIDOPARCIAL  = PrincipalStates(estado = 'ATENDPAR')
ARCHIVADO  = PrincipalStates(estado = 'ARCH')

ENPROYECTO.save()
PARADESPACHO.save()
EMITIDO.save()
RECIBIDO.save()
RECIBIDOPARCIAL.save()
ATENDIDO.save()
ATENDIDOPARCIAL.save()
ARCHIVADO.save()



tag1 = TagModel(txtTag='Solicita recursos')
tag2 = TagModel(txtTag='Invitacion evento')
tag3 = TagModel(txtTag='Decreto urgencia')
tag4 = TagModel(txtTag='Solicita informacion')
tag5 = TagModel(txtTag='Informativo')

tag1.save()
tag2.save()
tag3.save()
tag4.save()
tag5.save()


mesa = User.objects.create_user(username='mesadepartes', password='mesadepartes', email='mesadepartes@onpe.com')
mesa.save()

mesaInterna = InternalUser(user=mesa,nombres='mesa',apellidos='mesa',codigoUsuario='mesa',codDependencia='mesa',dependencia='mesa')
mesaInterna.save()


user = User.objects.create_user(username='Victor', password='Victor', email='Victor@onpe.com')
user.save()

iu = InternalUser(user=user,nombres='Victor',apellidos='Chura',codigoUsuario='11',codDependencia='SI',dependencia='SI')
iu.save()

ri = RegisteredInstitutions(institutionName='local',urlInstitution='181.224.226.157',puerto=8000)
ri.save()

rmayo = RegisteredInstitutions(institutionName='MAYO',urlInstitution='52.170.220.211',puerto=8000)
rmayo.save()

rpcm = RegisteredInstitutions(institutionName='PCM',urlInstitution='13.82.181.237',puerto=8000)
rpcm.save()






