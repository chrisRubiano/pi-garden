import serial
from django.shortcuts import render
from gpiozero import OutputDevice


def all_sensors_view(request):
    led = OutputDevice(17)
    context_dict = {}
    ser = serial.Serial('/dev/ttyUSB0')
    led.on()
    ser.write(b's\n')
    while True:
        if (ser.in_waiting>0):
            data = ser.readline()
            led.off()
            data = data.decode("ASCII")
            data = data.rstrip()
            ser.close()
            break
    context_dict['temp'] = data
    return render(request, 'sensors/all_sensors.html', context_dict)
    
