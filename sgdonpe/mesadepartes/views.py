from django.shortcuts import render
from sgdonpe.mesadepartes.forms import UploadFileMesaDePartes
from sgdonpe.activities import UtilFunctions
from sgdonpe.authentication.models import InternalUser
from django.http import JsonResponse
# Create your views here.
def presentar(request):
    if request.method == "POST":
        print('mesa de partes presentar isPost')
        return presentarPorSGD(request)
    else:
        print('mesa de partes presentar isPGET')
        return presentarCiudadano(request)
#metodo GET
def presentarCiudadano(request):
    form = UploadFileMesaDePartes()
    return render(request, 'mesadepartes/loadfile.html',
                      {'form': form})

#metodo POST
def presentarPorSGD(request):
    pass

def handleLoadFile(request):
    if request.method == "POST":
        dict = request.POST
        print('mesa de partes handleLoadFile isPost')
        if 'nombre' in dict and 'apellido' in dict and 'dni':
            if 'title' in dict and 'file' in dict and 'internalUser' in dict:
                idInternalUser = dict['internalUser']
                possibleInternalUser = InternalUser.objects.filter(pk=idInternalUser)
                if len(possibleInternalUser) > 0:
                    internalUser = possibleInternalUser[0]
                    docPk = UtilFunctions.handle_citizen_uploadfile(title=dict['title'],file=dict['file'],
                                                            internalUser=internalUser,
                                                            nombre=dict['nombre'],
                                                            apellido=dict['apellido'],
                                                            dni=dict['dni'])
                    f = {}
                    f['docPK'] = docPk
                    return JsonResponse(f)
        f = {}
        f['nada'] = True
        return JsonResponse(f)
    else:
        print('handleLoadFile isPGET')
        return presentarCiudadano(request)