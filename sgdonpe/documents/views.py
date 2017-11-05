from django.shortcuts import render
import json
from sgdonpe.documents.models import Document
from sgdonpe.documents.forms import UploadFileForm
from sgdonpe.historiers.forms import SelectActivityForm, SelectInternalUserForm, SelectDocumentToReference
from django.contrib.auth.decorators import login_required
from sgdonpe.mesadepartes import views
# Create your views here.
@login_required
def documents(request):
    if request.method == "POST":
        print('isPost')
        UploadFileForm.upload_file(request)
    else:
        print('isNotPost')
    all_documents = Document.get_documents(request.user)
    listReferences = [doc.getAllReferences() for doc in all_documents]
    listTags = [doc.getAllTags() for doc in all_documents]
    all_documents = zip(all_documents,listReferences,listTags)
    form = UploadFileForm()
    formActivity = SelectActivityForm()
    json_str = views.getUsersAsJSON()
    json_objects = json.loads(json_str)

    selectUser = [ (id_user, json_objects[id_user]) for id_user in json_objects]

    selectReference  = SelectDocumentToReference()
    return render(request, 'documents/documents.html', {
        'documents': all_documents,
        'form': form,
        'comboBox': formActivity,
        'idUserNombreUser': selectUser,
        'comboFiles': selectReference,
        })