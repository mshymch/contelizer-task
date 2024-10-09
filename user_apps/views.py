from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .models import UploadedFile
from .functions import mix_middle_chars


# Create your views here.
def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def display_file(request):
    uploaded_file = UploadedFile.objects.last()

    # When there is no file redirect to upload page
    try:
        with uploaded_file.file.open('r') as f:
            file_content = f.read()
            output_content = mix_middle_chars(file_content)

        # Delete the file from the server
        uploaded_file.file.delete(save=False)  # Delete file from storage
        uploaded_file.delete()  # Delete entry from DB

    except Exception as e:
        return redirect('/text')

    return render(request, 'display.html', {'file_content': output_content})
