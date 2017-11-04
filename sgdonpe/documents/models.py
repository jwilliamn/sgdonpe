from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DocumentComment(models.Model):
    documento = models.ForeignKey('Document')
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = "Comentario del documento"
        verbose_name_plural = "Comentarios del documento"
        ordering = ("date",)

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.article.title)


class DocumentFile(models.Model):
    file = models.FileField(upload_to='docFiles/')
    fileName = models.CharField(max_length=200)


class DocumentoOficial(models.Model):
    fileID = models.ForeignKey(DocumentFile, on_delete=models.CASCADE)


class Anexo(models.Model):
    idFile = models.ForeignKey(DocumentFile, on_delete=models.CASCADE)
    nextanexoID = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Document(models.Model):

    title = models.CharField(max_length=255, null=False, unique=True)
    content = models.TextField(max_length=4000)
    owner_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    docOficialID = models.ForeignKey(DocumentoOficial)
    firstAnexoID = models.ForeignKey(Anexo, null=True)
    estado = models.CharField(max_length=16, null=False, default='NA')

    class Meta:
        verbose_name = ("Documento")
        verbose_name_plural = ("Documentos")
        ordering = ("-create_date",)

    def __str__(self):
        return self.title


    @staticmethod
    def get_enviados():
        articles = Document.objects.filter(status=Document.ENVIADO)
        return articles

    @staticmethod
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
    @staticmethod
    def get_documents(from_document=None):
        if from_document is not None:
            documents = Document.objects.filter(parent=None, id__lte=from_document)
        else:
            documents = Document.objects.all()
        return documents




    def get_resumen(self):
        if len(self.content) > 255:
            return '{0}...'.format(self.content[:255])
        else:
            return self.content

    def get_cantidadAnexos(self):
        return 0

    def get_comments(self):
        return DocumentComment.objects.filter(article=self)

    def get_current_state(self):
        return self.status

