


import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(f):
    file_type = f.name.split('.')[-1]

    
    if file_type == 'csv':
        df = pd.read_csv(f)
    else:
        df = pd.read_excel(f)
        

    return df

def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
           
            df = handle_uploaded_file(request.FILES['file'])
            
            table_html = df.to_html(classes='table table-striped', index=False)
            return render(request, 'summary.html', {'table_html': table_html})
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})
