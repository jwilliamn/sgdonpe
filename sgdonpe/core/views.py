from django.shortcuts import render
from sgdonpe.documents.views import documents
from sgdonpe.mesadepartes.models import RegisteredInstitutions
from sgdonpe.historiers.models import PrincipalStates

from django.contrib.auth.models import User
from sgdonpe.documents.models import TagModel
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return documents(request)
    else:
        return render(request, 'core/cover.html')
def inicializar(request):
    ENPROYECTO = PrincipalStates(estado='ENPROYEC')
    PARADESPACHO = PrincipalStates(estado='PARADESP')
    EMITIDO = PrincipalStates(estado='EMITIDO')
    RECIBIDO = PrincipalStates(estado='RECIB')
    RECIBIDOPARCIAL = PrincipalStates(estado='RECIBPAR')
    ATENDIDO = PrincipalStates(estado='ATEND')
    ATENDIDOPARCIAL = PrincipalStates(estado='ATENDPAR')
    ARCHIVADO = PrincipalStates(estado='ARCH')

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

    user = User.objects.create_user(username='mesadepartes', password='mesadepartes',
                                    email='mesadepartes@mesadepartes.com')
    user.save()

    return JsonResponse({})
