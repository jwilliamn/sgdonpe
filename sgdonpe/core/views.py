from django.shortcuts import render
from sgdonpe.documents.views import documents
# Create your views here.
def home(request):
    if request.user.is_authenticated():
        return documents(request)
    else:
        return render(request, 'core/cover.html')