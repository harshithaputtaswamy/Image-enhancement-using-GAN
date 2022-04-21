# from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

def index(request):
    return render(request, 'Image_Enhancement/index.html')

def send_to_model(f):
    #TODO
    print(f)
def receive_from_model():
    #TODO
    pass
def display(output):
    #TODO--geetha will do
    #just copy paste the below function code for overwriting the file name and storing in media folder
    return render(request, 'Image_Enhancement/index.html')
def upload(request):
    if request.method == 'POST':
        if len(request.FILES) == 0:
            print("not uploaded")
            return HttpResponse("Hello, world. You have not chosen any file.")#TODO - have to change 

        myfile=request.FILES['myfile']
        myfile._name = "InputFile."+ myfile._name.split('.')[1]#renaming the file
        
        #the below code checks whether the filename exists in the directory or not
        fullname = os.path.join(settings.MEDIA_ROOT, myfile.name)
        if os.path.exists(fullname):
            os.remove(fullname)#if it exists it overwrite the file with the new file

        fs = FileSystemStorage() 
        input_file = fs.save(myfile.name, myfile)# file in storing in media folder

        send_to_model(input_file) 
    return HttpResponse("Hello, world. You have uploaded.")
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'Image_Enhancement/index.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    
    
