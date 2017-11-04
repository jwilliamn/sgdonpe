from django.shortcuts import render
import json
from sgdonpe.documents.models import Document
from sgdonpe.documents.forms import UploadFileForm
from sgdonpe.historiers.forms import SelectActivityForm, SelectInternalUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def documents(request):
    if request.method == "POST":
        print('isPost')
        UploadFileForm.upload_file(request)
    else:
        print('isNotPost')
    all_documents = Document.get_documents()
    form = UploadFileForm()
    formActivity = SelectActivityForm()
    selectUser = SelectInternalUserForm()

    return render(request, 'documents/documents.html', {
        'documents': all_documents,
        'form': form,
        'comboBox': formActivity,
        'comboUser': selectUser,
        })