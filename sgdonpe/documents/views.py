from django.shortcuts import render
import json
from sgdonpe.documents.models import Document
from sgdonpe.documents.forms import UploadFileForm
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
    return render(request, 'documents/documents.html', {
        'documents': all_documents,
        'form': form
        })