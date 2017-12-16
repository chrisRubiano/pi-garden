import serial
from django.shortcuts import render


def temp_view(request):
    context_dict = {}
    ser = serial.Serial('/dev/ttyUSB0')
    ser.write(b's\n')
    while True:
        if (ser.inWaiting()>0):
            data = ser.readline()
            data = data.decode("ASCII")
            data = data.rstrip()
            ser.close()
            break
    context_dict['temp'] = data
    return render(request, 'sensors/temp.html', context_dict)
    
