from django.shortcuts import render
from sgdonpe.historiers.views import documentHistory
from sgdonpe.authentication.models import InternalUser
from sgdonpe.remitos.models import Remito
# Create your views here.
from django.contrib.auth.decorators import login_required
from sgdonpe.documents.models import DocumentViewer,Document
import datetime
@login_required
def sendFile(request,idDocument):
    if request.user.is_authenticated():
        if request.method == 'POST':
            print(request.POST)

            if 'users' in request.POST:
                codUser = request.POST['users']
                internalUserPossible = InternalUser.objects.filter(pk=codUser)
                if len(internalUserPossible)>0:
                    targetUser = internalUserPossible[0].user
                    originUser = request.user
                    allPossibleDocuments = Document.objects.filter(pk=idDocument)
                    if len(allPossibleDocuments) > 0:

                        # we should add targetUser as a viewer
                        document = allPossibleDocuments[0]
                        docViewer = DocumentViewer(user=targetUser,document=document)
                        docViewer.save()

                        internalUserTarget = InternalUser.findInternalUser(targetUser)
                        internalUserOrigin = InternalUser.findInternalUser(originUser)

                        remito = Remito(tipo='ADMI',
                                        codigo=str(document.pk),
                                        estado='EMITIDO',
                                        codigoDependenciaRemitente=internalUserOrigin.codDependencia,
                                        dependenciaRemitente=internalUserOrigin.dependencia,
                                        codigoEncargadoRemitente=internalUserOrigin.codigoUsuario,
                                        encargadoRemitente = str(internalUserOrigin),
                                        ruc= '11415069511',
                                        personaJuridica = 'personaJuridica',
                                        dni='415069510',
                                        ciudadano = 'ciudadano',
                                        codigoTipoDoc= 'abc',
                                        descripcionTipoDoc=document.title,
                                        numeroDoc=str(document.pk),
                                        fecha = datetime.datetime.now(),
                                        asunto =document.title)
                        remito.save()
                        print('remito saved:')
    return documentHistory(None,idDocument)

@login_required
def addReference(request,idDocument):
    if request.user.is_authenticated():
        if request.method == 'POST':
            print(request.POST)
            if 'references' in request.POST:
                codReference = request.POST['references']
                possibleReferenced = Document.objects.filter(pk=codReference)
                possibleParentReferencing = Document.objects.filter(pk=idDocument)

                if len(possibleReferenced) >0 and len(possibleParentReferencing) >0:
                    docReferenced = possibleReferenced[0]
                    docParentReferencing = possibleParentReferencing[0]
                    docParentReferencing.addDocReference(docReferenced)

    return documentHistory(None, idDocument)