# from django.shortcuts import render
from pyexpat.errors import messages
from ssl import AlertDescription
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from . import test_funieGAN
from django.contrib import messages

def index(request):
    return render(request, 'Image_Enhancement/index.html')


def send_to_model():
    test_funieGAN.test_model()

    
def upload(request):
    if request.method == 'POST':
        if len(request.FILES) == 0:
            print("not uploaded")
            # return HttpResponse("You have not chosen any file.")
            messages.info(request, "Info! Choose file to perform enhancement")
            return render(request, 'Image_Enhancement/index.html', {
            
        })

        myfile=request.FILES['myfile']

        fs = FileSystemStorage() 
        input_file = fs.save('input/' + myfile.name, myfile)
        print(input_file)
        test_funieGAN.test_model(myfile.name) 

        output_file_url = settings.MEDIA_URL + 'output/' + myfile.name
        print(output_file_url, '\n\n\n')
        uploaded_file_url = fs.url(input_file)
        return render(request, 'Image_Enhancement/index.html', {
            'uploaded_file_url': uploaded_file_url,
            'output': output_file_url
        })
    
    
