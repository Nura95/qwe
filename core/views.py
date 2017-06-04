from django.shortcuts import render
from django.http import HttpResponse
from core.forms import UploadFileForm
from .utils import handle_uploaded_file
from .models import File
def index(request):
    return HttpResponse("Hello, world.")
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('/success/url/')
    else:
        form = UploadFileForm()
        return render(request,'home.html', {'form': form})




