import serial
from django.shortcuts import render
from gpiozero import OutputDevice
from time import sleep


def all_sensors_view(request):
    try:
        led = OutputDevice(17)
        context_dict = {}
        ser = serial.Serial('/dev/ttyUSB0')
        sleep(2)
        ser.write(b's\n')
        while True:
            if (ser.in_waiting>0):
                data = ser.readline()
                data = data.decode("ASCII")
                data = data.rstrip()
                break
        context_dict['temp'] = data
        return render(request, 'sensors/all_sensors.html', context_dict)
    except:
        context_dict = {}
        return render(request, 'sensors/all_sensors.html', context_dict)
    finally:
        led.off()
        ser.close()