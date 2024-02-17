from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse

from .forms import UploadFileForm


def handle_uploaded_file(f):
    with open(f"pictures/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    if(request.method == 'POST'):
        #handle_uploaded_file(request.FILES['file_upload'])
        form = UploadFileForm(request.POST,request.FILES)
        #<p><input type="file" name="file_upload"></p>
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    return render(request,'main/index.html',{'form':form})
    #return render(request,'main/index.html')
# Create your views here.
def about(request):
    return render(request,'main/about.html')
# Create your views here.
