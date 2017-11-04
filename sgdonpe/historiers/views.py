from django.shortcuts import render
import json
from sgdonpe.historiers.models import StepHistory
from django.contrib.auth.decorators import login_required
from sgdonpe.documents.models import  Document
from sgdonpe.historiers.models import PrincipalStates
# Create your views here.

def documentHistory(request,idDocument):

    all_history = StepHistory.getAllHistory(idDocument)

    return all_history

@login_required
def addHistory(request,idDocument):
    print('idDocumento: ',idDocument)
    if request.method == "POST":
        print('isPost')
        print('POST:: ',request.POST)
        if 'principalState' in request.POST:
            pstate_cod = request.POST['principalState']
            pstate = PrincipalStates(estado=pstate_cod)
            pstate.save()
        else:
            pstate = StepHistory.get_last_principalState(idDocument)
        if pstate is None:
            pstate = PrincipalStates()
            pstate.save()

        if 'comentario' in request.POST:
            comentario = request.POST['comentario']
        else:
            comentario = 'Sin comentario'
        qsDocument = Document.objects.filter(pk=idDocument)
        if len(qsDocument) > 0:
            document = qsDocument[0]
            stepHistory = StepHistory(document=document,currentPrincipalStateID=pstate, user=request.user,comentario=comentario)
            stepHistory.save()

    else:
        print('isNotPost')

    return documentHistory(None, idDocument)


#document = models.ForeignKey(Document)
   # currentPrincipalStateID = models.ForeignKey(PrincipalStates)
   # externUserID = models.IntegerField()
  #  user = models.ForeignKey(User)
 #   when = models.DateField(auto_now_add=True)
#    previousStepHistory = models.ForeignKey('self', null=True)


