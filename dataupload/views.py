import pandas as pd
import io
from django.shortcuts import render
from django.contrib import messages

def upload_data(request):
    file_type  = request.POST.get('source')
    db_host  = request.POST.get('db_host')
    db_huser  = request.POST.get('db_huser')
    password  = request.POST.get('password')
    db_name  = request.POST.get('db_name')
    db_table  = request.POST.get('db_table')
    sql_query  = request.POST.get('sql_query')
    upload_type  = request.POST.get('upload_type')
    csv_data = []
    link  = request.POST.get('link')
    file = request.FILES['file']
    if file_type == 'csv':
        try:
            if upload_type == "local":
                csv_data = pd.read_csv(io.StringIO(file.read().decode("utf-8")))
            elif(upload_type == 'online'):
                csv_data = pd.read_csv(link)
            else:
                messages.error(request, 'Invalid upload type')
                return render(request, 'data/data_acquisition.html')
            column_headers = list(csv_data.columns)
        except Exception as e:
            messages.error(request, 'Error occured while reading csv...')
            print (e)
            return render(request, 'data/data_acquisition.html')
    else:
        messages.error(request, 'Invalid file type')
        return render(request, 'data/data_acquisition.html')
    # if csv_data:
    #     for data in csv_data.to_dict(orient="records"):


    return render(request, 'data/view_data.html',{'columns':column_headers,'csv_data':csv_data.to_dict(orient="records")})
    


