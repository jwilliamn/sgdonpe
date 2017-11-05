from django.shortcuts import render
from sgdonpe.mesadepartes.forms import UploadFileMesaDePartes, DocumentSearcher
from sgdonpe.activities import UtilFunctions
from sgdonpe.authentication.models import InternalUser,ExternalUser
from sgdonpe.historiers.models import StepHistory
from sgdonpe.documents.models import Document
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

def searchDocument(request):
    form = DocumentSearcher()
    return render(request, 'mesadepartes/documentSearcher.html',
                  {'form': form})

def buscarPORDNI(request):
    if request.method == 'POST':
        if 'dni' in request.POST:
            externUsersWithDNI = ExternalUser.objects.filter(dni=request.POST['dni'])
            print('Usuario Externo: ',externUsersWithDNI)

            allDocuments = [sh.document for sh in StepHistory.objects.filter(externUserID__in=externUsersWithDNI)]
            print('AllDcouments ', allDocuments)

            return render(request, 'mesadepartes/documents.html',
                          {'documents': allDocuments})
    f= {}
    f['error']=True
    return JsonResponse(f)
#metodo POST
def presentarPorSGD(request):
    if request.method == "POST":
        dict = request.POST
        print('dict in presentarPorSGD:',dict)
        if 'nombre' in dict and 'apellido' in dict and 'dni' and 'codigoUsuario' in dict:
            if 'title' in dict and 'file' in dict and 'internalUser' in dict:
                if 'sgdUrl' in dict and 'depend' in dict and 'codDependencia' in dict:
                    idInternalUser = dict['internalUser']
                    possibleInternalUser = InternalUser.objects.filter(pk=idInternalUser)
                    if len(possibleInternalUser) > 0:
                        internalUser = possibleInternalUser[0]
                        docPk =UtilFunctions.handle_sgd_uploadfile(title=dict['title'],
                                                                   file=dict['file'],
                                                                   internalUser=internalUser,
                                                                   nombre=dict['nombre'],
                                                                   apellido=dict['apellido'],
                                                                   dni=dict['dni'],
                                                                   codigoUsuario=dict['codigoUsuario'],
                                                                   codDependencia=dict['codDependencia'],
                                                                   dependencia=dict['dependencia'],
                                                                   urlUser=dict['urlUser'])
                        f = {}
                        f['docPK'] = docPk
                        return JsonResponse(f)
    f = {}
    f['nadapresentarPorSGD'] = True
    return JsonResponse(f)

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