from django import forms

from sgdonpe.documents.models import Document
from django.contrib.auth.models import User
from django.shortcuts import render

class UploadFileForm(forms.Form):

    def confirm_login_allowed(self, user):
        pass


    title = forms.CharField(max_length=50)
    file = forms.FileField()
    @staticmethod
    def upload_file(request):
        if request.user.is_authenticated():
            print('it is authenticated')
            if request.method == 'POST':
                print(request.POST)
                print(request.FILES)
                Document.handle_uploaded_file(request.POST['title'], request.POST['file'], request.user)

                return render(request, 'core/cover.html')
            else:
                return render(request, 'core/cover.html')
        else:
            print('not authenticated')
            return render(request, 'core/cover.html')


