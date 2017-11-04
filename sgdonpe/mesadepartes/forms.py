from django import forms
from sgdonpe.authentication.models import InternalUser
from sgdonpe.documents.models import Document
from django.shortcuts import render
class UploadFileMesaDePartes(forms.Form):
    internalUser = forms.ModelChoiceField(queryset=InternalUser.objects.all())
    nombre = forms.CharField(max_length=64,empty_value="nombre")
    apellido = forms.CharField(max_length=64, empty_value="apellido")
    dni = forms.CharField(max_length=64, empty_value="dni")
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    @staticmethod
    def upload_file(request):

        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            possibleUsers = InternalUser.objects.filter(pk=request.POST['internalUser'])
            if len(possibleUsers)>0:

                cod_expediente = Document.handle_citizen_uploadfile(title=request.POST['title'],
                                                                    file=request.POST['file'],
                                                                    internalUser=possibleUsers[0],
                                                                    nombre=request.POST['nombre'],
                                                                    apellido=request.POST['apellido'],
                                                                    dni=request.POST['dni'])
                print('upload by citizen handled', cod_expediente)
                return render(request, 'core/cover.html')
            else:
                return render(request, 'core/cover.html')

        else:
            return render(request, 'core/cover.html')