from django.shortcuts import render
from sgdonpe.historiers.views import documentHistory
from sgdonpe.authentication.models import InternalUser
from sgdonpe.remitos.models import Remito
# Create your views here.
from django.contrib.auth.decorators import login_required
from sgdonpe.documents.models import DocumentViewer,Document
from sgdonpe.historiers.models import StepHistory
from sgdonpe.activities import UtilFunctions
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
                        principalState = StepHistory.getLastState(document)
                        UtilFunctions.handleEnvioDocumento(originUser=originUser,
                                                           targetUser=targetUser,
                                                           principalState=principalState,
                                                           document=document)




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