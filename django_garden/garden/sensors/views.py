import serial
from django.shortcuts import render
from gpiozero import OutputDevice


def all_sensors_view(request):
    try:
        led = OutputDevice(17)
        context_dict = {}
        ser = serial.Serial('/dev/ttyUSB0')
        led.on()
        led.off()
        ser.write(b's\n')
        while True:
            if (ser.in_waiting>0):
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
        return render(request, 'pages/home.html', context_dict)
    finally:
        led.close()

