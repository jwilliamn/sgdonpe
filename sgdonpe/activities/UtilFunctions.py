from sgdonpe.documents.models import DocumentFile,Document,DocumentViewer, DocumentoOficial
from sgdonpe.authentication.models import InternalUser,ExternalUser
from sgdonpe.remitos.models import Remito
from sgdonpe.historiers.models import StepHistory,PrincipalStates
import datetime

def handle_citizen_uploadfile(title, file, internalUser, nombre, apellido, dni):
    docFile = DocumentFile(file=file, fileName=title)
    docFile.save()
    print('docFileSaved')
    documentoOficial = DocumentoOficial(fileID=docFile)
    documentoOficial.save()
    print('documentoOficial Saved')
    mesaDePartes = InternalUser.getUserMesaDePartes()
    print('mesaDePartes:',mesaDePartes)
    document = Document(title=title,
                        content=title,
                        owner_user=mesaDePartes,
                        docOficialID=documentoOficial,
                        )
    document.save()

    externalUser = ExternalUser.createExternalCitizenUser(nombres=nombre,
                                                          apellidos=apellido,
                                                          dni=dni)
    externalUser.save()
    handleEnvioDocumentoExterno(externalUser=externalUser,document=document)
    handleEnvioDocumento(mesaDePartes,internalUser.user,StepHistory.getLastState(document),document,True)

    return document.pk
   # nombres = models.CharField(max_length=64)
   # apellidos = models.CharField(max_length=64)
   # codigoUsuario = models.CharField(max_length=8)
   # codDependencia = models.CharField(max_length=8,default='ING')
   # dependencia = models.CharField(max_length=256)
   # urlUser = models.CharField(max_length=128)
   # dni = models.CharField(max_length=12)
def handle_sgd_uploadfile(title, file, internalUser, nombre, apellido, dni,
                          codigoUsuario, codDependencia,dependencia,urlUser):
    docFile = DocumentFile(file=file, fileName=title)
    docFile.save()
    print('docFileSaved')
    documentoOficial = DocumentoOficial(fileID=docFile)
    documentoOficial.save()
    print('documentoOficial Saved')
    mesaDePartes = InternalUser.getUserMesaDePartes()
    print('mesaDePartes:',mesaDePartes)
    document = Document(title=title,
                        content=title,
                        owner_user=mesaDePartes,
                        docOficialID=documentoOficial,
                        )
    document.save()

    externalUser = ExternalUser(nombres=nombre,
                                apellidos=apellido,
                                dni=dni,
                                codigoUsuario=codigoUsuario,
                                codDependencia=codDependencia,
                                dependencia=dependencia,
                                urlUser=urlUser)
    externalUser.save()
    handleEnvioDocumentoExterno(externalUser=externalUser,document=document)
    handleEnvioDocumento(mesaDePartes,internalUser.user,StepHistory.getLastState(document),document,True)

    return document.pk


def handle_uploaded_file(titleFile, fileItself, authenticatedUser):
    print('loading file:',titleFile)
    docFile = DocumentFile(file=fileItself, fileName=titleFile)
    docFile.save()
    documentoOficial = DocumentoOficial(fileID=docFile)
    documentoOficial.save()
    document = Document(title=titleFile,
                        content='AsuntoUnico',
                        owner_user=authenticatedUser,
                        docOficialID=documentoOficial)
    document.save()
    docViewer = DocumentViewer(user = authenticatedUser, document = document)
    docViewer.save()
def handleEnvioDocumentoExterno(externalUser,document):
    mesaDePartes = InternalUser.getUserMesaDePartes()
    docViewer = DocumentViewer(user=mesaDePartes, document=document)
    docViewer.save()
    stepHistory = StepHistory(document=document,
                              currentPrincipalStateID=StepHistory.getLastState(document),
                              user=mesaDePartes,
                              externUserID=externalUser,
                              comentario='usuario externo: '+str(externalUser) + ' envio a ' + str(mesaDePartes))
    stepHistory.save()

def handleEnvioDocumento(originUser,targetUser,principalState,document,withRemito=True):
    internalUserTarget = InternalUser.findInternalUser(targetUser)
    internalUserOrigin = InternalUser.findInternalUser(originUser)

    docViewer = DocumentViewer(user=targetUser, document=document)
    docViewer.save()

    stepHistory = StepHistory(document=document,
                              currentPrincipalStateID=principalState,
                              user=originUser,
                              comentario=str(originUser) + ' envio a ' + str(targetUser))
    stepHistory.save()

    if withRemito:
        remito = Remito(tipo='ADMI',
                        codigo=str(stepHistory.pk),
                        estado=str(principalState),
                        codigoDependenciaRemitente=internalUserOrigin.codDependencia,
                        dependenciaRemitente=internalUserOrigin.dependencia,
                        codigoEncargadoRemitente=internalUserOrigin.codigoUsuario,
                        encargadoRemitente=str(internalUserOrigin),
                        ruc='11415069511',
                        personaJuridica='personaJuridica',
                        dni='415069510',
                        ciudadano='ciudadano',
                        codigoTipoDoc='abc',
                        descripcionTipoDoc=document.title,
                        numeroDoc=str(document.pk),
                        fecha=datetime.datetime.now(),
                        asunto=document.title)
        remito.save()
        print('remito saved:')


    print('envio registered')