from django.http import JsonResponse
from django.shortcuts import render
import csv
import struct
import os
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def landingurl(request):
    return render(request,'landingpage.html')
@csrf_exempt
def filesub(request):
    print('ok')
    data=request.FILES['filename']
    print(data) 
    return JsonResponse({'msg':'ok'})

def csv_to_dat(csv_file_path, dat_file_path,skip_header=True):
    # Open the CSV file for reading
    csv_path =Path(csv_file_path)
    dat_path = Path(dat_file_path)
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        if skip_header:
            next(csv_reader)
        
        # Open the DAT file for writing
        with open(dat_file_path, 'wb') as dat_file:
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Convert the row values to bytes using the desired format
                # Here, we assume that each value is a floating-point number
                row_bytes = struct.pack('f' * len(row), *map(float, row))
                
                # Write the bytes to the DAT file
                dat_file.write(row_bytes)
