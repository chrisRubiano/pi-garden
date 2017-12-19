import serial
from django.shortcuts import render
from gpiozero import OutputDevice
import ipdb;


def all_sensors_view(request):
    try:
        led = OutputDevice(17)
        context_dict = {}
        ser = serial.Serial('/dev/ttyUSB0')
        ser.write(b's\n')
        while True:
            if (ser.in_waiting>0):
                ipdb.set_trace()
                data = ser.readline()
                led.on()
                data = data.decode("ASCII")
                data = data.rstrip()
                ser.close()
                led.off()
                break
        context_dict['temp'] = data
        return render(request, 'sensors/all_sensors.html', context_dict)
    except:
        context_dict = {}
        return render(request, 'sensors/all_sensors.html', context_dict)
    finally:
        led.off()
        led.close()

