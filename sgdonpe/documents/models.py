from django.db import models
from django.contrib.auth.models import User
from sgdonpe.authentication.models import InternalUser
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

class DocumentViewer(models.Model):
    user = models.ForeignKey(User)
    document = models.ForeignKey('Document')


class DocReferences(models.Model):
    docParentReferencing = models.ForeignKey('Document',
                                             related_name='el_nuevo_documento', null = True)
    docChildReferenced = models.ForeignKey('Document', related_name='el_antiguo_documento',null=True)


class TagModel(models.Model):
    txtTag = models.CharField(max_length=24)

    def __str__(self):
        return self.txtTag


class DocTags(models.Model):
    document = models.ForeignKey('Document')
    tag = models.ForeignKey(TagModel)


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
    def get_documents(from_document=None):
        if from_document is not None:
            lista_pk = [dv.document.pk for dv in DocumentViewer.objects.filter(user=from_document)]
            print('para: ',from_document,lista_pk)
            documents = Document.objects.filter(pk__in = lista_pk)
        else:
            documents = Document.objects.all()
        return documents




    def addDocReference(self, docReferencing):
        linkReferencing = DocReferences(docParentReferencing=self,docChildReferenced=docReferencing)
        linkReferencing.save()

    def getAllReferences(self):
        allReferences = DocReferences.objects.filter(docParentReferencing=self)
        return [ref.docChildReferenced for ref in allReferences]

    def getAllTags(self):
        allDocTags = DocTags.objects.filter(document=self)
        return [docTag.tag for docTag in allDocTags]

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

