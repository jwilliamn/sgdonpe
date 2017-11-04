from django.shortcuts import render
from sgdonpe.historiers.views import documentHistory
from sgdonpe.authentication.models import InternalUser
# Create your views here.
from django.contrib.auth.decorators import login_required


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
                    fromUser = request.user


    return documentHistory(None,idDocument)