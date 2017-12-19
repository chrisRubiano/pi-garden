import serial
from django.shortcuts import render
from gpiozero import OutputDevice
from time import sleep


def get_sensor_data():
    try:
        led = OutputDevice(17)
        led.on()
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
    except:
        data = "Error!"
    finally:
        led.off()
        ser.close()
        return data

def all_sensors_view(request):
    context_dict = {}
    data = get_sensor_data()
    context_dict['temp'] = data
    return render(request, 'sensors/all_sensors.html', context_dict)