from django.shortcuts import render
import json
from sgdonpe.documents.models import Document
from sgdonpe.documents.forms import UploadFileForm
from sgdonpe.historiers.forms import SelectActivityForm, SelectInternalUserForm, SelectDocumentToReference
from django.contrib.auth.decorators import login_required
from sgdonpe.mesadepartes import views
from sgdonpe.mesadepartes.models import RegisteredInstitutions
from sgdonpe.mesadepartes.forms import SelectInstitutionToReference
import http.client, urllib
import codecs
# Create your views here.
@login_required
def documents(request):
    if request.method == "POST" and 'externalSGD' not in request.POST:
        print('isPost')
        UploadFileForm.upload_file(request)
    else:
        print('it will not updateFile')
    all_documents = Document.get_documents(request.user)
    listReferences = [doc.getAllReferences() for doc in all_documents]
    listTags = [doc.getAllTags() for doc in all_documents]
    all_documents = zip(all_documents,listReferences,listTags)
    form = UploadFileForm()
    formActivity = SelectActivityForm()
    idUrl = 'local'
    if 'externalSGD' in request.POST:
        idInstitucion = request.POST['externalSGD']
        possibleInstitutions = RegisteredInstitutions.objects.filter(pk=idInstitucion)
        if len(possibleInstitutions)>0:
            reader = codecs.getreader("utf-8")
            response = getExternalUsrs(possibleInstitutions[0].urlInstitution,possibleInstitutions[0].puerto)
            json_str = response.decode('utf8')
            json_objects = json.loads(json_str)
            idUrl = possibleInstitutions[0].pk
        else:
            json_str = views.getUsersAsJSON()
            json_objects = json.loads(json_str)
    else:
        json_str = views.getUsersAsJSON()
        json_objects = json.loads(json_str)


    selectUser = [ (id_user, json_objects[id_user]) for id_user in json_objects]

    selectReference  = SelectDocumentToReference()
    selectInstitution = SelectInstitutionToReference()

    return render(request, 'documents/documents.html', {
        'documents': all_documents,
        'form': form,
        'comboBox': formActivity,
        'idUserNombreUser': selectUser,
        'comboFiles': selectReference,
        'comboInstitutions': selectInstitution,
        'idUrl': idUrl
        })

def getExternalUsrs(urlInstitution,puerto):
    print(urlInstitution,puerto)
    params = urllib.parse.urlencode({'nombre': 'Victor',
                               'codigoUsuario': 'codUser'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # conn = http.client.HTTPConnection("http://127.0.0.1:8000/")
    conn = http.client.HTTPConnection(urlInstitution, puerto)
    conn.request("GET", "/mesadepartes/getUsers/", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    return data